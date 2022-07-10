#include<stdio.h>
#include<ctype.h>

char stack[100];
int top = -1;

char pop() {
	if(top == -1) {
		return -1;
	}
	else {
		return stack[top--];
	}
}

void push(char ch) {
	stack[++top] = ch;
}

int priority(char ch) {
	if (ch == '(') {
		return 0;
	}
	if (ch == '+' || ch == '-') {
		return 1;
	}
	if (ch == '/' || ch == '*') {
		return 2;
	}
	return 0;
}

int main() {
	char *x, ch, a = 0, space = 0;
	char line[256];
	
	FILE* f=fopen("infix_input.txt", "r");
	
	while(fgets(line, sizeof(line), f)) {
		if(space != 0) {
			printf("\n");
		}
		x=line;
		
		while(*x != '\0') {
			
			if(isalnum(*x)) {
				printf("%c ", *x);
			}
			else if(*x == '(') {
				push(*x);
			}
			else if(*x == ')') {
				while((ch = pop()) != '(') {
					printf("%c ", ch);
				}
			}
			else {
				while(priority(stack[top]) > priority(*x)) {
					printf("%c ", pop());
				}
				push(*x);
			}
			x++;
		}
		space++;	
	}
	
	while(top != -1) {
		printf("%c ", pop());
	}
	
	fclose(f);
	return 0;
}
