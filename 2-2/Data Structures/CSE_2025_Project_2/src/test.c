#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
//graph_created
// Read
// create graph pointer
// add edge fucn() ---> a new node is add to the adjacency list of source node
// add all
// run dijkstra with graph pointer and source node
// dijkstra --> createminHeap(v) v= number node
//



// Adjacency list nodes of the graph
struct Datas{
    int n; // Number of vertices
    int edges; // Number of edges
    int *weightArray;
    char *srcArray;
    char *destArray;
    char *vertices;

};

struct Node
{
    char dest;
    int weight;
    struct Node* next;
};

struct Graph
{
    int n;
    struct Node* *array;
};

struct Graph* createGraph(struct Datas* data)
{
    struct Graph* graph = (struct Graph*) malloc(sizeof (struct Graph));
    graph->n = data->n;
    graph->array = (struct Node**) malloc(data->n * sizeof (struct Node));

    for (int i = 0; i < data->n; ++i) {
        graph->array[i] = NULL;
    }
    int index;
    for (int j = 0; j < data->edges; ++j)
    {

        char tmpSrc = data->srcArray[j];
        char tmpDest = data->destArray[j];
        int tmpWeight = data->weightArray[j];

        for (int k = 0; k < data->n; ++k)
        {

            if (tmpSrc == data->vertices[k])
            {
                index = k;
                break;
            }
        }
        // Src -> Dest
        struct Node* newNode = (struct Node*)malloc(sizeof (struct Node));
        newNode->dest = tmpDest;
        newNode->weight = tmpWeight;
        newNode->next = graph->array[index];
        graph->array[index] = newNode;

        // Dest-> Src
        for (int l = 0; l < data->n; ++l) {
            if(tmpDest == data->vertices[l])
            {
                index = l;
                break;
            }
        }

        newNode = (struct Node*)malloc(sizeof (struct Node));
        newNode->dest = tmpSrc;
        newNode->weight = tmpWeight;
        newNode->next = graph->array[index];
        graph->array[index] = newNode;

        
    }
    return graph;
}
struct Node* traverse(struct Node* ptr)
{
    if(ptr == NULL)
        return NULL;
    traverse(ptr->next);
    printf("%c,%d ",ptr->dest,ptr->weight);

}
void printGraph(struct Graph* *graph,struct Datas* data)
{
    int i;
    struct Graph* tmpGraph = *graph;
    for (i = 0; i < data->n; i++)
    {
        printf("%c: ",data->vertices[i]);
        // print current vertex and all its neighbors
        struct Node* ptr = tmpGraph->array[i];
        traverse(ptr);
        printf("\n");
    }
}

void ReadFile(struct Datas* data,struct Graph* *graph)
{

    char letter;
    char filename[256];
    printf("Enter the file name: \n");
    scanf("%s",filename);

    FILE *fp = fopen(filename,"r");

    int line_count = 0;

    while (!feof(fp)) {
        char vertex, trash1;
        int trash2;

        fscanf(fp, " %c,%c,%d", &vertex, &trash1, &trash2);
        line_count++;
    }
    fclose(fp);

    data->srcArray = NULL;
    data->destArray= NULL;
    data->weightArray = NULL;

//    data->srcArray = (char *) malloc(line_count * sizeof (char));
//    data->destArray = (char *) malloc(line_count * sizeof(char));
//    data->weightArray = (int *) malloc(line_count * sizeof(int));
//    data->vertices = (char *) malloc(line_count * sizeof(char));
    data->srcArray = (char *) calloc(line_count, sizeof (char ));
    data->destArray = (char *) calloc(line_count, sizeof(char ));
    data->weightArray = (int *) calloc(line_count, sizeof(int ));
    data->vertices = (char *) calloc(line_count, sizeof(char ));


    int vertexCount = 0;
    int  i = 0;

    fp = fopen(filename,"r");

    while (!feof(fp)) {
        char src, dest;
        int weight;

        fscanf(fp, " %c,%c,%d", &src, &dest, &weight);
        data->srcArray[i] = src;
        data->destArray[i] = dest;
        data->weightArray[i] = weight;
        i++;
    }
    data->edges = line_count;
    fclose(fp);
    i=0;

    for (int j = 0; j < data->edges; ++j) {
        if (letter != data->srcArray[j])
        {
            data->vertices[vertexCount] = data->srcArray[j];
            //vertexList[vertexCount] = srcList[j];
            vertexCount++;

        }
        letter = data->srcArray[j];
    }


    //printf("%d\n",vertexCount);
    char tmpVertex;
    int check = 0;
    for (int k = 0; k < data->edges; ++k)
    {
        letter = data->destArray[k];
        //letter = destList[k];
        for (int l = 0; l < vertexCount ; ++l)
        {
            tmpVertex = data->vertices[l];
            //tmpVertex = vertexList[l];
            if (letter == tmpVertex)
                check = 1;
        }
        if (check == 0)
        {
            data->vertices[vertexCount] = letter;
            //vertexList[vertexCount] = letter;
            vertexCount++;
        }
        check = 0;
    }
    data->n = vertexCount;

    //printf("\n%d %d\n",data->n,data->edges);

    *graph = createGraph(data);

    //printGraph(*graph,data);

}
//data store struct
void UI(struct Datas* data)
{
    int operation;
    struct Graph *graph = NULL;

    bool check = true;
    while(check)
    {
        printf("Please select an operation: \n 1. Read file\n 2. Show adjacency list \n 3. Find shortest path\n 4. Exit\n");
        scanf(" %d", &operation);
        switch (operation)
        {
            case 1:
                printf("read file\n");
                ReadFile(data,&graph);
                break;
            case 2:
                printf("print list\n");
                printGraph(&graph,data);
                break;
            case 3:
                printf("find shortest path\n");
                break;
            case 4:
                printf("exit");
                check = false;
                break;
            default:
                printf("Invalid operation!\n");
        }
    }
}

int main(){
    struct Datas *data = (struct Datas*)malloc(sizeof (struct Datas));
    struct Graph *graph;
    printf("Hello World\n");
    printf("\n");
    //ReadFile(data);
    //printf("\n%d %d\n",data->n,data->edges);

    UI(data);
    return 0;
}