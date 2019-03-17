// Author: Nika Otiashvili
// K&R exercise 2-2

#include <stdio.h>

#define lim 100
int main(void)
{
     char s[lim];
     char c;

     printf("Input characters until newline:\n");
     for (int i=0; i < lim-1; ++i) {
	  if ((c = getchar()) == '\n')
	       break;
	  if (c == EOF)
	       break;
	  s[i] = c;
     }

     printf("Chars were %s\n", s);
     return 0;
}
