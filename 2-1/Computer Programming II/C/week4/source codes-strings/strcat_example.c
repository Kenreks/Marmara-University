#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[])
{
   /* Define a temporary variable */
   char example[100];
   char example2[100];

   int day = 3;
   int year = 2018;
   char *month = "May";
   /* Copy the first string into the variable */
   strcpy(example, "I like ");

   /* Concatenate the following two strings to the end of the first one */
   strcat(example, "CSE1142 course ");
   strcat(example, "a lot.");
   
   /* Display the concatenated strings */
   printf("%s\n", example);

   sprintf(example2,"Today is %s %d %d", month, day, year);
   printf("%s\n", example2);

   return 0;
}
