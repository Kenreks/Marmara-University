#include <stdio.h>
void genie(void)
{
	static int wish = 0; /* value is kept in memory */
	wish++;
	if ( wish <= 3)
		printf("What is your %d. wish?\n", wish);
	else
		printf("No more wishes.\n");
}
int main()
{
	int i;
	for (i=1; i<=5; i++) /* call genie() five times */
		genie();
}
