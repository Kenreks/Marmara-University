#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[])
{
    char input[100];
    int i, palindrome=1;

    scanf("%s",input);
    printf("Input:%s\n", input);

    for(i=0;i<strlen(input)/2;i++){
        if(input[i]!=input[strlen(input)-1-i]){
            palindrome=0;
            break;
        }
    }
    if(palindrome)
        printf("%s is a palindrome",input);
    else
        printf("%s is not a palindrome",input);
    return 0;
}
