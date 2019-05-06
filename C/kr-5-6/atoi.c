// Author: Nikoloz Otiashvili
// K&R Exercise 5-6 (atoi)

#include <stdio.h>

int atoi_p(char *s);

int main(void)
{
     printf("%i\n", atoi_p("1918"));
     return 0;
}


/* Converts s to integer using pointers */
int atoi_p(char *s)
{
     int n;
     n = 0;
     while (*s)
	  n = 10 * n + (*s++ - '0');
     return n;
}
