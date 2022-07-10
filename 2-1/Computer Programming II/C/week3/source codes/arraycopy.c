#include <stdio.h>

void arraycopy(int src[], int dest[], int size){
	for(int i=0; i<size; i++)
		dest[i] = src[i];
}

int main(){
	int a1[5] = {3,7,2,8,5};
	int a2[5];
	arraycopy(a1, a2, 5);
	
	for(int i=0; i<5; i++)
		printf("%d ", a2[i]);
} 
