#include <stdio.h>

int arraycomp(int a[], int b[], int size){
	for(int i=0; i<size; i++)
		if(a[i] != b[i])
				return 0;
	return 1;
}

int main(){	
	int a1[5] = {3,7,2,8,5};
	int a2[5] = {3,7,2,8,5};
	int a3[5] = {3,7,2,5,8};
	printf("a1 == a2 is %s\n", arraycomp(a1, a2, 5) ? "True":"False");
	printf("a1 == a3 is %s\n", arraycomp(a1, a3, 5) ? "True":"False");
	printf("a2 == a3 is %s\n", arraycomp(a2, a3, 5) ? "True":"False");
} 
