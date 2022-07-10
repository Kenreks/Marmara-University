#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <math.h>
#include <stdbool.h>

typedef struct line{

    time_t time;
    char validBit;
    int tag;
    char *data;

}line;

typedef struct set{

    line *lines;

}set;

void setGlobalVariables(char *argv[]);
void createCaches(set *L1I, set *L1D, set *L2);
void setValidBitsToZero(set *L1I, set *L1D, set *L2);
void traceFile(set *L1I, set *L1D, set *L2);

void loadInstructionOrData(bool loadInstruction, char *cacheName, set *L1I, set *L1D, set *L2, char *address, int size);
void dataStore(set *L1D, set *L2, char *address, int size, char *data);
void dataModify(set *L1I, set *L1D, set *L2, char *address, int size, char *data);

int returnLineNumberIfStored(set *L, int lineNumber, int setNum, int tag);
int copyInstructionBetweenCaches(set *source, set *dest, int sourceLineNumber, int sourceSetNum, int destSetNum, int destTag, int destTotalLine, int destBlockSize);
int copyInstructionFromRamToL2Cache(int int_address, set *L2, int setNumL2, int tagL2);
void copyDataToRAM(int int_address, int size, char *data);
void printSummary(char *cacheName, int hit, int miss, int eviction);
void cleanUp(set *L1I, set *L1D, set *L2);

//Global variables.
int L1s, L1E, L1b, L2s, L2E, L2b, L1S, L1B, L2S, L2B;
char *fileName;

//Hit, miss, eviction counters.
int L1I_hit = 0, L1I_miss = 0, L1I_eviction = 0;
int L1D_hit = 0, L1D_miss = 0, L1D_eviction = 0;
int L2_hit = 0, L2_miss = 0, L2_eviction = 0;

//Loop iterators.
int i, j;

int main(int argc, char *argv[]){

    //Firstly, checking if the user entered correct number of command-line arguments.
    if(argc == 1){
        printf("You didn't enter any command-line arguments. Please enter them.\n");
        return 0;
    }else if(argc < 15){
        printf("You entered %d number of command-line arguments, but you need to enter 14 values.\n", (argc-1));
        return 0;
    }

    //Setting the global variables as the user entered.
    setGlobalVariables(argv);

    /////////////////////////////////////////////////////////////////////////////////////////////

    //Lets create caches.
    set L1I[L1S];
    set L1D[L1S];
    set L2[L2S];

    createCaches(L1I, L1D, L2);

    //After creating the caches, we need to make sure their valid bit is 0 initially.
    setValidBitsToZero(L1I, L1D, L2);

    /////////////////////////////////////////////////////////////////////////////////////////////

    //Now, we need to read the trace file.
    traceFile(L1I, L1D, L2);

    /////////////////////////////////////////////////////////////////////////////////////////////

    //Printing the results.
    printf("\n");
    printSummary("L1I", L1I_hit, L1I_miss, L1I_eviction);
    printSummary("L1d", L1D_hit, L1D_miss, L1D_eviction);
    printSummary("L2", L2_hit, L2_miss, L2_eviction);
    printf("\n");

    cleanUp(L1I, L1D, L2);
    return 0;
}

void setGlobalVariables(char *argv[]){

    L1s = (int) strtol(argv[2], NULL, 10);
    L1E = (int) strtol(argv[4], NULL, 10);
    L1b = (int) strtol(argv[6], NULL, 10);
    L2s = (int) strtol(argv[8], NULL, 10);
    L2E = (int) strtol(argv[10], NULL, 10);
    L2b = (int) strtol(argv[12], NULL, 10);
    fileName = argv[14];

    L1S = (int) pow(2, L1s);
    L2S = (int) pow(2, L2s);

    L1B = (int) pow(2, L1b);
    L2B = (int) pow(2, L2b);
}

void createCaches(set *L1I, set *L1D, set *L2){

    int blockSizeL1 = (int) pow(2, L1b);
    int blockSizeL2 = (int) pow(2, L2b);

    //Allocating space for lines and datas.
    for(i = 0; i < L1S; i++){
        L1I[i].lines = malloc(L1E * sizeof(line));
        L1D[i].lines = malloc(L1E * sizeof(line));

        //Setting the block sizes.
        for(j = 0; j < L1E; j++){
            L1I[i].lines[j].data = malloc(blockSizeL1 * sizeof(char));
            L1D[i].lines[j].data = malloc(blockSizeL1 * sizeof(char));
        }
    }

    //Same thing for L2 cache.
    for(i = 0; i < L2S; i++){
        L2[i].lines = malloc(L2E * sizeof(line));

        //Setting the block sizes.
        for(j = 0; j < L2E; j++)
            L2[i].lines[j].data = malloc(blockSizeL2 * sizeof(char));
    }
}

void setValidBitsToZero(set *L1I, set *L1D, set *L2){

    for(i = 0; i < L1S; i++){
        for(j = 0; j < L1E; j++){

            L1I[i].lines[j].validBit = 0;
            L1D[i].lines[j].validBit = 0;

        }
    }

    for(i = 0; i < L2S; i++){
        for(j = 0; j < L2E; j++){

            L2[i].lines[j].validBit = 0;

        }
    }
}

void traceFile(set *L1I, set *L1D, set *L2){

    FILE *fp = NULL;

    //If the file exists, we read it. If not, we exit the function with an error.
    if(access(fileName, F_OK) != -1){

        fp = fopen(fileName, "r");

    }else{

        printf("%s does not exist. Please make sure it exists before starting this program.\n", fileName);
        return;
    }

    //Variables.
    char operation;
    int size;
    char address[16], data[16];

    //After reading the file, its time to read its content.
    //While not reaching to the end of file, we will read it.
    while(!feof(fp)) { // NOLINT

        if(fscanf(fp, "%c", &operation) == 1){

            //Now, we will look at the "operation" to understand which operation to execute.
            switch(operation){

                case 'I':

                    if(fscanf(fp, " %[^,] , %d\n", address, &size) == 2){ // NOLINT

                        printf("\nI %s, %d", address, size);
                        loadInstructionOrData(true, "L1I", L1I, L1D, L2, address, size);

                    }

                    break;
                case 'L':

                    if(fscanf(fp, " %[^,] , %d\n", address, &size) == 2){ // NOLINT

                        printf("\nL %s, %d", address, size);
                        loadInstructionOrData(false, "L1D", L1I, L1D, L2, address, size);

                    }

                    break;
                case 'S':

                    if(fscanf(fp, " %[^,] , %d , %s\n", address, &size, data) == 3){ // NOLINT

                        printf("\nS %s, %d, %s", address, size, data);
                        dataStore(L1D, L2, address, size, data);

                    }

                    break;
                case 'M':

                    if(fscanf(fp, " %[^,] , %d , %s\n", address, &size, data) == 3){ // NOLINT

                        printf("\nM %s, %d, %s", address, size, data);
                        dataModify(L1I, L1D, L2, address, size, data);

                    }

                    break;
                default:

                    //If we encounter any weird symbol it means this file is corrupted. We return from the function.
                    printf("\nThe program encountered an invalid operation type, exiting...\n");
                    return;
            }
        }
    }

    fclose(fp);
}

void loadInstructionOrData(bool loadInstruction, char *cacheName, set *L1I, set *L1D, set *L2, char *address, int size){

    //At the start of the function, we need to tell program which set to use for the rest of the function.
    set *setToUse;

    if(loadInstruction)
        setToUse = L1I;
    else
        setToUse = L1D;


    //First, we need to convert the address into an appropriate format and also convert hex to decimal.
    int int_address = (int) strtol(address, NULL, 16);

    //Getting necessary information.
    int blockNumL1 = int_address & ((int) pow(2, L1b) - 1); // NOLINT
    int setNumL1 = (int_address >> L1b) & ((int) pow(2, L1s) - 1); // NOLINT
    int tagSizeL1 = 32 - (L1s + L1b);
    int tagL1 = (int_address >> (L1s + L1b)) & ((int) pow(2, tagSizeL1) - 1); // NOLINT

    int blockNumL2 = int_address & ((int) pow(2, L2b) - 1); // NOLINT
    int setNumL2 = (int_address >> L1b) & ((int) pow(2, L2s) - 1); // NOLINT
    int tagSizeL2 = 32 - (L2s + L2b);
    int tagL2 = (int_address >> (L2s + L2b)) & ((int) pow(2, tagSizeL2) - 1); // NOLINT

    //Checking if the data can fit into cache block.
    if(blockNumL1 + size > L1B || blockNumL2 + size > L2B){

        //Means the data can't fit. We need to return.
        printf("\nCan't fit the data for the size of wanted block. Please edit your trace file...\n");
        exit(0);

    }

    printf("\n   ");

    //Then, we need to check if the instruction is in caches.
    int L1_location = returnLineNumberIfStored(setToUse, L1E, setNumL1, tagL1);
    int L2_location = returnLineNumberIfStored(L2, L2E, setNumL2, tagL2);

    if(L1_location != -1){

        ////////////////////////////////// HIT IN L1
        printf("%s hit", cacheName);
        (loadInstruction == true) ? L1I_hit++ : L1D_hit++;

        //Lets update the time variable.
        setToUse[setNumL1].lines[L1_location].time = time(NULL);

        //Now, lets check if the instruction is in L2 cache.
        if(L2_location != -1){

            ////////////////////////////////// HIT IN L1 AND L2
            printf(", L2 hit\n");
            L2_hit++;

            //Lets update the time variable.
            L2[setNumL2].lines[L2_location].time = time(NULL);

        }else{

            ////////////////////////////////// HIT IN L1 BUT MISS IN L2
            //Means the instruction is in L1 cache but not stored in L2 cache. So we need to copy it from L1.
            printf(", L2 miss\n");
            L2_miss++;

            L2_eviction += copyInstructionBetweenCaches(setToUse, L2, L1_location, setNumL1, setNumL2, tagL2, L2E, L2B);

        }

    }else{

        ////////////////////////////////// MISS IN L1
        printf("%s miss", cacheName);
        (loadInstruction == true) ? L1I_miss++ : L1D_miss++;

        //After that, we need to check if the instruction is stored in L2 cache.
        if(L2_location != -1) {

            ////////////////////////////////// MISS IN L1 BUT HIT IN L2
            //The instruction is in L2 cache.
            printf(", L2 hit\n");
            L2_hit++;

            //Lets update the time variable.
            L2[setNumL2].lines[L2_location].time = time(NULL);

            //Now, we need to load it into L1 cache.
            int eviction_counter = copyInstructionBetweenCaches(L2, setToUse, L2_location, setNumL2, setNumL1, tagL1, L1E, L1B);

            if(loadInstruction) L1I_eviction += eviction_counter;
            else L1D_eviction += eviction_counter;

        }else{

            ////////////////////////////////// MISS IN BOTH L1 AND L2
            printf(", L2 miss\n");
            L2_miss++;

            //The instruction is not in L1 neither in L2. So we need to load it from RAM.
            L2_location = copyInstructionFromRamToL2Cache(int_address, L2, setNumL2, tagL2);
            int eviction_counter = copyInstructionBetweenCaches(L2, setToUse, L2_location, setNumL2, setNumL1, tagL1, L1E, L1B);

            if(loadInstruction) L1I_eviction += eviction_counter;
            else L1D_eviction += eviction_counter;

        }
    }

    printf("   Place in L2 set %d, %s set %d\n", setNumL2, cacheName, setNumL1);
}

void dataStore(set *L1D, set *L2, char *address, int size, char *data){

    //First, we need to convert the address into an appropriate format and also convert hex to decimal.
    int int_address = (int) strtol(address, NULL, 16);

    //Also, we need to convert the data to a an appropriate format.
    char char_data[size], subString[2];

    for(int a = 0; a < size; a++){

        strncpy(subString, (data + a * 2), 2);
        char_data[a] = (char) strtol(subString, NULL, 16);

    }

    //Getting necessary information.
    int blockNumL1 = int_address & ((int) pow(2, L1b) - 1); // NOLINT
    int setNumL1 = (int_address >> L1b) & ((int) pow(2, L1s) - 1); // NOLINT
    int tagSizeL1 = 32 - (L1s + L1b);
    int tagL1 = (int_address >> (L1s + L1b)) & ((int) pow(2, tagSizeL1) - 1); // NOLINT

    int blockNumL2 = int_address & ((int) pow(2, L2b) - 1); // NOLINT
    int setNumL2 = (int_address >> L1b) & ((int) pow(2, L2s) - 1); // NOLINT
    int tagSizeL2 = 32 - (L2s + L2b);
    int tagL2 = (int_address >> (L2s + L2b)) & ((int) pow(2, tagSizeL2) - 1); // NOLINT

    //Checking if the data can fit into cache block.
    if(blockNumL1 + size > L1B || blockNumL2 + size > L2B){

        //Means the data can't fit. We need to return.
        printf("\nCan't fit the data for the size of wanted block. Please edit your trace file...\n");
        exit(0);

    }

    printf("\n   ");

    //Then, we need to check if the data is in caches.
    int L1D_location = returnLineNumberIfStored(L1D, L1E, setNumL1, tagL1);
    int L2_location = returnLineNumberIfStored(L2, L2E, setNumL2, tagL2);

    if(L1D_location != -1) {

        ////////////////////////////////// HIT IN L1D
        printf("L1D hit");
        L1D_hit++;

        //Now, we need to store our data in L1D.
        L1D[setNumL1].lines[L1D_location].time = time(NULL);
        memcpy(L1D[setNumL1].lines[L1D_location].data, char_data, (size_t) size);

        //Now, lets check if the data is in L2 cache.
        if(L2_location != -1) {

            ////////////////////////////////// HIT IN L1D AND L2
            printf(", L2 hit\n");
            L2_hit++;

            //Lets store this data in L2 too.
            L2[setNumL2].lines[L2_location].time = time(NULL);
            memcpy(L2[setNumL2].lines[L2_location].data, char_data, (size_t) size);

        }else{

            ////////////////////////////////// HIT IN L1D BUT MISS IN L2
            //Means the data is in L1D cache but not stored in L2 cache. So we need to copy it from L1D.
            printf(", L2 miss\n");
            L2_miss++;

            L2_eviction += copyInstructionBetweenCaches(L1D, L2, L1D_location, setNumL1, setNumL2, tagL2, L2E, L2B);

        }

    }else{

        ////////////////////////////////// MISS IN L1D
        printf("L1D miss");
        L1D_miss++;

        //After that, we need to check if the data is stored in L2 cache.
        if(L2_location != -1) {

            ////////////////////////////////// MISS IN L1D BUT HIT IN L2
            //The data is in L2 cache.
            printf(", L2 hit\n");
            L2_hit++;

            //Now, we need to load this data into L1D cache.
            L1D_eviction += copyInstructionBetweenCaches(L2, L1D, L2_location, setNumL2, setNumL1, tagL1, L1E, L1B);

        }else{

            ////////////////////////////////// MISS IN BOTH L1D AND L2
            printf(", L2 miss\n");
            L2_miss++;

            //The instruction is not in L1D neither in L2. So we need to load it from RAM.
            L2_location = copyInstructionFromRamToL2Cache(int_address, L2, setNumL2, tagL2);
            L1D_eviction = copyInstructionBetweenCaches(L2, L1D, L2_location, setNumL2, setNumL1, tagL1, L1E, L1B);

        }

        //Now, we caught all misses and evictions and datas are in both L1D and L2 caches.

        //Make the changes. For this, we need the line number.
        L1D_location = returnLineNumberIfStored(L1D, L1E, setNumL1, tagL1);

        L1D[setNumL1].lines[L1D_location].time = time(NULL);
        memcpy(L1D[setNumL1].lines[L1D_location].data, char_data, (size_t) size);

        //Also, we need to copy this data from L1D back to L2 cache.
        copyInstructionBetweenCaches(L1D, L2, L1D_location, setNumL1, setNumL2, tagL2, L2E, L2B);
    }

    //We have updated the data in caches now. All we need to do is copy the data from L2 cache back to RAM.
    copyDataToRAM(int_address, size, char_data);

    printf("   Store in L1D, L2, RAM\n");
}

void dataModify(set *L1I, set *L1D, set *L2, char *address, int size, char *data){

    //Data modify is simply a data load followed by a data store.

    loadInstructionOrData(false, "L1D", L1I, L1D, L2, address, size);
    dataStore(L1D, L2, address, size, data);

}

int returnLineNumberIfStored(set *L, int lineNumber, int setNum, int tag){

    int i;

    //First, we need to check if the corresponding line is valid and is it contains the data.
    for(i = 0; i < lineNumber; i++){

        //We will look if the valid bit is 1 and also the tag matches.
        if(L[setNum].lines[i].validBit == 1 && L[setNum].lines[i].tag == tag)
            return i;
    }

    return -1;
}

int copyInstructionBetweenCaches(set *source, set *dest, int sourceLineNumber, int sourceSetNum, int destSetNum, int destTag, int destTotalLine, int destBlockSize){

    //Return value. 1 if there is an eviction, 0 if there is no eviction.
    int returnValue = 0;

    bool freeSlot = false;
    int lineToPlace = 0;

    for(i = 0; i < destTotalLine; i++){

        if(dest[destSetNum].lines[i].validBit == 0){
            freeSlot = true;
            lineToPlace = i;
            break;
        }
    }

    //If freeSlot is false, it means all the lines are valid so we have an eviction.
    if(freeSlot == false){

        returnValue++;

        //Now, we need to determine which line to use. For this we need to look at time_t values.
        time_t current = time(NULL);

        for(i = 0; i < destTotalLine; i++){

            if(current > dest[destSetNum].lines[i].time){
                current = dest[destSetNum].lines[i].time;
                lineToPlace = i;
            }
        }
    }

    //Now, we have determined which line to store our instruction.
    dest[destSetNum].lines[lineToPlace].validBit = 1;
    dest[destSetNum].lines[lineToPlace].tag = destTag;
    dest[destSetNum].lines[lineToPlace].time = time(NULL);
    memcpy(dest[destSetNum].lines[lineToPlace].data, source[sourceSetNum].lines[sourceLineNumber].data, (size_t) destBlockSize);

    return returnValue;
}

int copyInstructionFromRamToL2Cache(int int_address, set *L2, int setNumL2, int tagL2){

    FILE *RAM = fopen("RAM.dat", "r");

    //We need to make sure to pull the right chunk of data.
    int address = int_address & (0xFFFFFFFF ^ (L2B - 1)); // NOLINT

    fseek(RAM, address, SEEK_SET);

    char readData[L2B];
    fread(readData, (size_t) L2B, 1, RAM);

    //We have gathered the data from the RAM.
    fclose(RAM);

    //Now, we need to store this data into the L2 cache.
    bool freeSlot = false;
    int lineToPlace = 0;

    for(i = 0; i < L2E; i++){

        if(L2[setNumL2].lines[i].validBit == 0){
            freeSlot = true;
            lineToPlace = i;
            break;
        }
    }

    //If freeSlot is false, it means all the lines are valid so we have an eviction.
    if(freeSlot == false){

        L2_eviction++;

        //Now, we need to determine which line to use. For this we need to look at time_t values.
        time_t current = time(NULL);

        for(i = 0; i < L2E; i++){

            if(current > L2[setNumL2].lines[i].time){
                current = L2[setNumL2].lines[i].time;
                lineToPlace = i;
            }
        }
    }

    //Now, we have determined which line to store our instruction.
    L2[setNumL2].lines[lineToPlace].validBit = 1;
    L2[setNumL2].lines[lineToPlace].tag = tagL2;
    L2[setNumL2].lines[lineToPlace].time = time(NULL);
    memcpy(L2[setNumL2].lines[lineToPlace].data, readData, (size_t) L2B);

    return lineToPlace;
}

void copyDataToRAM(int int_address, int size, char *data){

    FILE *RAM = fopen("RAM.dat", "r+");

    fseek(RAM, int_address, SEEK_SET);

    //Write the data here.
    fwrite(data, 1, (size_t) size, RAM);

    //We have wrote the data to the RAM.
    fclose(RAM);
}

void printSummary(char *cacheName, int hit, int miss, int eviction){

    printf("\n%s-hits: %d %s-misses: %d %s-evictions: %d", cacheName, hit, cacheName, miss, cacheName, eviction);

}

void cleanUp(set *L1I, set *L1D, set *L2){

    //Freeing L1 cache.
    for(i = 0; i < L1S; i++){

        //Firstly, we need to free data pointers.
        for(j = 0; j < L1E; j++){
            free(L1I[i].lines[j].data);
            free(L1D[i].lines[j].data);
        }

        //Now, we can free lines.
        free(L1I[i].lines);
        free(L1D[i].lines);
    }

    //Same things for L2 cache.
    for(i = 0; i < L2S; i++){

        //Firstly, we need to free data pointers.
        for(j = 0; j < L2E; j++)
            free(L2[i].lines[j].data);

        //Now, we can free lines.
        free(L2[i].lines);
    }
}
