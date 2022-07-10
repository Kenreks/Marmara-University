#include <stdio.h>
#include <stdlib.h>
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
    char *srcArray;
    char *destArray;
    int *weightArray;
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

struct Graph* createGraph(char src[],char dest[],int n,int numberOfEdge,char vertexList[],int weightList[])
{
    struct Graph* graph = (struct Graph*) malloc(sizeof (struct Graph));
    graph->n = n;
    graph->array = (struct Node**) malloc(n * sizeof (struct Node));

    for (int i = 0; i < n; ++i) {
        graph->array[i] = NULL;
    }
    int index;
    for (int j = 0; j < numberOfEdge; ++j)
    {

        char tmpSrc = src[j];
        char tmpDest = dest[j];
        char tmpWeight = weightList[j];

        for (int k = 0; k < n; ++k)
        {

            if (tmpSrc == vertexList[k])
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
        for (int l = 0; l < n; ++l) {
            if(tmpDest == vertexList[l])
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
void printGraph(struct Graph* graph,int n,char vertexList[])
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%c: ",vertexList[i]);
        // print current vertex and all its neighbors
        struct Node* ptr = graph->array[i];
        traverse(ptr);
        printf("\n");
    }
}

void ReadFile(struct Datas* data)
{

    char letter;
    char filename[] = "input.txt";
    //printf("Enter the file name: \n");

    FILE *fp = fopen(filename,"r");

    int line_count = 0;

    while (!feof(fp)) {
        char vertex, trash1;
        int trash2;

        fscanf(fp, " %c,%c,%d", &vertex, &trash1, &trash2);
        line_count++;
    }
    fclose(fp);

    char srcList[line_count];
    char destList[line_count];
    int  weightList[line_count];
    char  vertexList[line_count];
    int vertexCount = 0;
    int  i = 0;

    fp = fopen(filename,"r");

    while (!feof(fp)) {
        char src, dest;
        int weight;

        fscanf(fp, " %c,%c,%d", &src, &dest, &weight);
        srcList[i] = src;
        destList[i] = dest;
        weightList[i] = weight;
        i++;
    }
    data->edges = line_count;
    fclose(fp);


    for (int j = 0; j < line_count; ++j) {
        if (letter != srcList[j])
        {
            vertexList[vertexCount] = srcList[j];
            vertexCount++;

        }
        letter = srcList[j];
    }


    //printf("%d\n",vertexCount);
    char tmpVertex;
    int check = 0;
    for (int k = 0; k < line_count; ++k)
    {
        letter = destList[k];
        for (int l = 0; l < vertexCount ; ++l)
        {
            tmpVertex = vertexList[l];
            if (letter == tmpVertex)
                check = 1;

        }
        if (check == 0)
        {

            vertexList[vertexCount] = letter;
            vertexCount++;
        }
        check = 0;
    }
    data->n = vertexCount;

    printf("\n%d %d\n",data->n,data->edges);
    struct Graph *graph = createGraph(srcList,destList,vertexCount,line_count,vertexList,weightList);

    printGraph(graph,vertexCount,vertexList);

}
//data store struct
void UI()
{
    int operation;

    printf("Please select an operation: \n 1. Read file\n 2. Show adjacency list \n 3. Find shortest path\n 4. Exit\n");
    scanf(" %d", &operation);

    switch (operation) {
        case 1:
            printf("read file\n");
            break;
        case 2:
            printf("print list\n");
            break;
        case 3:
            printf("find shortest path\n");
            break;
        case 4:
            printf("exit");
            return;
        default:
            printf("Invalid operation!\n");
    } UI();
}

int main(){
    struct Datas *data = (struct Datas*)malloc(sizeof (struct Datas));
    printf("Hello World\n");
    printf("\n");
    ReadFile(data);
    printf("\n%d %d\n",data->n,data->edges);

    //UI();
    return 0;
}