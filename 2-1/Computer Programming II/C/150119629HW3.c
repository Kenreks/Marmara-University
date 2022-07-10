//Huseyin Kerem Mican 150119629
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { //String struct
    char str[50];
} String;

int charAt(String *s, int index) { // finds nth char
    int i, j;
    char array[strlen(s)+1];
    if (index >= strlen(s) || index < 0) {
        return -1;
    }
    strcpy(array, s);
    for (i = 0; i < strlen(s) - 1; i++) {
        if (array[i] == 32) {
            for (j = i; j < array[j] != '\0'; j++) {
                array[j] = array[j+1];
            }
        }
    }
    if (array[index] > 64 && array[index] < 91) { //checks for uppercase letters
    	return array[index];
	} else {
		return array[index] - 32;
	}
}

String *concat(String *s1, String *s2) { //combines two string
    int i;
    char array1[strlen(s1)], array2[strlen(s2)], array3[strlen(s1)+strlen(s2)];
    strcpy(array1, s1);
    strcpy(array2, s2);

    for (i = 0; i < strlen(array1); i++) { //appends first string to common array
        if (array1[i] < 65 && array1[i] != 32) {
            array1[i] = 32;
        }
        array3[i] = array1[i];
    }
    for (i = 0; i < strlen(array2); i++) { //appends second string to common array
        array3[i + strlen(array1) + 1] = array2[i];
    }
    if (array3[strlen(array1)] < 65 && array3[strlen(array1)] != 32) {
        array3[strlen(array1)] = 32;
    }
    for (i = 0; i < strlen(array3); i++) {
        if (array3[i] < 65 && array3[i] != 32 && array3[i] != 33) {
            array3[i] = '\0';
        }
    }
    return array3;
}

unsigned int strSearch(String *s1, String *s2) { //searchs for a specific string
	int i, j, k, z, count = 0, first, last, stop1 = 0, stop2 = 0;
    char array1[strlen(s1)], array2[strlen(s2)];
    strcpy(array1, s1);
    strcpy(array2, s2);

    for (i = 0; i < strlen(s1); i++) {
        for (j = 0; j < strlen(s2); j++) {
            if (array1[i] == array2[j]) {
                for (k = 1; k < strlen(s2); k++) {
                    if (array1[i+k] == array2[j+k]) {
                        count++;
                    }
                    if (count >= strlen(s2)) { //these lines finds spaces after and before a specific string and then find its length
                        for (z = 0; z < i; z++) {
                            if (array1[i-z] == 32 && stop1 == 0 && array1[i-z] < 65) {
                                first = i-z+1;
                                stop1 = 1;
                            }
                            if ((array1[i+z] == 32 || array1[i+z] == NULL || array1[i+z] < 65) && stop2 == 0) {
                                last = i+z;
                                stop2 = 1;
                            }
                        }
                    }
                }
            }
        }
    }
    printf("%d\n", last-first);
    return last-first;
}

unsigned int findScore(String *s1) { //finds the score of the sentence
	int i, score = 0;
    char array1[strlen(s1)];
    strcpy(array1, s1);

    for (i = 0; i < strlen(s1); i++) { //checks every single char and finds their score and add it to total score
        if (array1[i] < 91 && array1[i] > 64) {
            if (array1[i] == 'A' || array1[i] == 'E' || array1[i] == 'I' || array1[i] == 'O' || array1[i] == 'U' || array1[i] == 'L' || array1[i] == 'N' || array1[i] == 'R' || array1[i] == 'S' || array1[i] == 'T') {
                score += 1;
            } else if (array1[i] == 'D' || array1[i] == 'G') {
                score += 2;
            } else if (array1[i] == 'B' || array1[i] == 'C' || array1[i] == 'M' || array1[i] == 'P') {
                score += 3;
            } else if (array1[i] == 'F' || array1[i] == 'H' || array1[i] == 'V' || array1[i] == 'W' || array1[i] == 'Y') {
                score += 4;
            } else if (array1[i] == 'K') {
                score += 5;
            } else if (array1[i] == 'J' || array1[i] == 'X') {
                score += 8;
            } else if (array1[i] == 'Q' || array1[i] == 'Z') {
                score += 10;
            }
        } else {
            if (array1[i] == 'a' || array1[i] == 'e' || array1[i] == 'i' || array1[i] == 'o' || array1[i] == 'u' || array1[i] == 'l' || array1[i] == 'n' || array1[i] == 'r' || array1[i] == 's' || array1[i] == 't') {
                score += 1;
            } else if (array1[i] == 'd' || array1[i] == 'g') {
                score += 2;
            } else if (array1[i] == 'b' || array1[i] == 'c' || array1[i] == 'm' || array1[i] == 'p') {
                score += 3;
            } else if (array1[i] == 'f' || array1[i] == 'h' || array1[i] == 'v' || array1[i] == 'w' || array1[i] == 'y') {
                score += 4;
            } else if (array1[i] == 'k') {
                score += 5;
            } else if (array1[i] == 'j' || array1[i] == 'x') {
                score += 8;
            } else if (array1[i] == 'q' || array1[i] == 'z') {
                score += 10;
            }
        }
    }
    printf("%d\n", score);
    return score;
}

int main(int argc, char *argv[]) { //main function
    int i, j,  countlines = 0, total_length = 0, total_word_count = 0, index_count = 0;
	
    char const* const inputName = argv[1]; //created arguments, char arrays and opened files here
	char const* const outputName = argv[2];
    FILE *file = fopen(inputName,"r");
    FILE *o_file = fopen(outputName,"w");
    char line[256], chr;
    String sentence1;
    String sentence2;

    chr = getc(file); // getting num of lines
    while (chr != EOF) {
        if (chr == '\n') {
            countlines += 1;
        }
        chr=getc(file);
    }

    fclose(file);
    file = fopen(inputName,"r");

    while (fgets(line, sizeof line, file) != NULL) { //getting every line in input file
        int index, opr, length = 0, space_count = 0;
        index_count ++;

        for (i = 0; i < strlen(sentence1.str)+strlen(line); i++) { //wipes array
            sentence1.str[i] = '\0';
        }

        if (strstr(line, "exit") || strstr(line, "quit")) { //checks line and if it is exit or quit terminates the program
            printf("Program ends. Bye");
            fprintf(o_file ,"%s", "Program ends. Bye");
            fclose(o_file);
            break;
        }
        else if (strstr(line, "stat")) { //checks string and prints stats
            printf("The number of words: %d\n", total_word_count);
            printf("The number of alphabetic letters: %d\n", total_length);
            
        	fprintf(o_file ,"%s", "The number of words: ");
        	fprintf(o_file ,"%d\n", total_word_count);
        	fprintf(o_file ,"%s", "The number of alphabetic letters:  ");
        	fprintf(o_file ,"%d\n", total_length);
        }
        else { //if string is not stat or exit keeps running program and reading lines
            int cnt = 0, str2cnt = 0, str1cnt = 0;
            total_length +=2;
                for (j = 0; j < strlen(line); j++) {
                    if (line[j] == 58) { //checks for colon
                        opr = line[j+1] - 48;
                    } else if (line[j] == 44) { //checks for comma
                        if (line[j+1] - 48 < 10) {
                            index = line[j+1] - 48;
                        } else { //reads string after comma
                            for (i = j; i < strlen(line)-2; i++) {
                                sentence2.str[i-j] = line[i+1];
                                str2cnt++;
                            }
                            for (i = strlen(sentence2.str); i > str2cnt - 1; i--) {
                                    sentence2.str[i] = '\0';
                                }
                            total_word_count++;
                        }
                    }else { //reads string before numbers and colons
                        if (line[j] < 58 && line[j] >47) {

                        } else {
                            if (line[j] == 32) { //space
                                space_count ++;
                                cnt++;
                            }
                            sentence1.str[j] = line[j];
                            if (line[j] - 64 > 0 && line[j] != 33) { //if char is an letter, adds 1 to total length
                                total_length ++;
                                length++;
                            }
                        }
                    }
                }
                total_length -= space_count;
                total_word_count += space_count + 1;
            switch (opr) { //checks num of opr and runs functions with given arguments
                case 1: printf("%c\n", charAt(sentence1.str, index-1));;
                fprintf(o_file, "%c\n", charAt(sentence1.str, index-1));
                    break;
                case 2: printf("%s\n", concat(sentence1.str, sentence2.str));
                fwrite(concat(sentence1.str, sentence2.str), sizeof(char) , strlen(concat(sentence1.str, sentence2.str)), o_file);
                fprintf(o_file, "\n");
                    break;
                case 3: fprintf(o_file ,"%d\n", strSearch(sentence1.str, sentence2.str));;
                    break;
                case 4: fprintf(o_file ,"%d\n", findScore(sentence1.str));
                    break;
                default: printf("Wrong operator number!");
                    break;
            }
            }
        }
    fclose(file); //closing files
    fclose(o_file);
    return 0;
}
