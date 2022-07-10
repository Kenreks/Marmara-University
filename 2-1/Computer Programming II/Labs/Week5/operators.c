#include <stdio.h>

int main(){
	int n = 5, x;
	n++;     /* n = 6 */
	printf("n:%d\n",n);
    // n = n+1 OR n += 1 OR n++

    x=n++; 
    printf("x:%d n:%d\n",x,n);
    /* equals to following two commands:
    * x = n;
    * n++;
    */
    
    x=n--;   
    printf("x:%d n:%d\n",x,n);
    /* equals to following two commands:
    * x = n;
    * n--;
    */  
    
    x=++n;   
    printf("x:%d n:%d\n",x,n);
    /* equals to following two commands:
    * n++;
    * x = n;
    */  
    
    x=--n;   
    printf("x:%d n:%d\n",x,n);
    /* equals to following two commands:
    * n--;
    * x = n;
    */  
    
	
	return 0;
}
