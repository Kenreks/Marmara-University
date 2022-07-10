#include <stdio.h>

int main(){			
    
    char ch1, ch2;
	printf("Enter two single digit integers: ");
    scanf("%c %c", &ch1, &ch2);
    
    int answer;
	answer = (ch1 - '0') * (ch2 - '0');
	printf("Answer is %d\n", answer);
	
	
	return 0;
}
