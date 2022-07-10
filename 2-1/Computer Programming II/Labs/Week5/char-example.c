#include <stdio.h>

int main(){			
	int a=5002;
    
	char ch='0';  /* ASCII code of '0' is 48 */
	printf("ch:%c ascii of ch:%d\n",ch,ch);

	ch=ch+3;       /* ch = '3', ASCII code becomes 51 */
	printf("ch:%c ascii of ch:%d\n",ch,ch);
	
	a+=ch;        /* a = 5053 */
	printf("a:%d\n",a);

	ch+=a;        /* ch = ?, overflow and undefined behavior occurs */
	printf("ch:%c ascii of ch:%d\n",ch,ch);
	
	return 0;
}
