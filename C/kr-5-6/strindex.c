// Author: Nikoloz Otiashvili
// K&R Exrecise 5-6 (strindex)

#include <stdio.h>

int strindex_p(char *s, char *t);

int main(void)
{
     printf("%i\n", strindex_p("Hello, friend", "Hell"));
     printf("%i\n", strindex_p("Hello, friend", "end"));
     printf("%i\n", strindex_p("Hello, friend", "Yarr"));
     return 0;
}

/* Return index of t in s, -1 if none */
int strindex_p(char *s, char *t)
{
     char *start_s = s;
     char *start_t = t;
     while (*s) {
	  while (*s++ == *t++)
	       if (*t == 0)
		    return s - start_s - (t - start_t); /* Return index */
	  t = start_t;		/* Reset t */
     }
     return -1;
}
