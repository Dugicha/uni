// Author: Nikoloz Otiashvili
// K&R Exercise 5-4

#include <stdio.h>

int strend(char s[], char t[]);

int main(void)
{
     char test_string[] = "It is but a scratch!";
     printf("test_string = %s\n", test_string);
     printf("scratch - %i\n", strend(test_string, "scratch"));
     printf("scratch! - %i\n", strend(test_string, "scratch!"));
     printf("! - %i\n", strend(test_string, "!"));
     printf("\"\" - %i\n", strend(test_string, ""));
     printf("It is but a scratch! - %i\n", strend(test_string, "It is but a scratch!"));
     printf("It is but a scratch - %i\n", strend(test_string, "It is but a scratch"));
     
     return 0;
}

/* Returns 1 if s ends with t; Returns 0 otherwise */
int strend(char s[], char t[])
{
     for(size_t i = 0; s[i] != '\0'; i++) {
     	  for (size_t j = 0; s[i] == t[j]; i++, j++) {
	       if (s[i] == '\0')
		    return 1;
	  }
     }

     return 0;
}
