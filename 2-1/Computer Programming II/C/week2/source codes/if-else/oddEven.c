#include <stdio.h>

int main(){
    int num;

    printf("Enter number:");
    scanf("%d", &num);

    printf("%d is an ", num);

    if (num%2!=0)
        printf("odd ");
    else
        printf("even ");
    printf("number.\n");


    return 1;
}
