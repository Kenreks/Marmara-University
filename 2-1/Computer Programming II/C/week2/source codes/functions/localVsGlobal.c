#include <stdio.h>

int d=10;
void f(int d)
{
   d++;
   printf("in f(): d=%d\n",d);
}
int main()
{  d=30;
   f(d);
   printf("After first call to f(): d=%d\n",d);
   d+=20;
   f(d);
   printf("After second call to f(): d=%d\n",d);
}
