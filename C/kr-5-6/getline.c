// Author: Nikoloz Otiashvili
// K&R Exercise 5-6 (getline)

#include <stdio.h>
#define MAXLINE 1000

/* Asks user for input with getline (pointer version) and prints character count
   of input line */

int getline_p(char *s, int lim);

int main(void)
{
     int len;
     char line[MAXLINE];
     while ((len = getline_p(line, MAXLINE)) > 0)
	  printf("\n%i characters in '%s' \n", len, line);
     return 0;
}

/* Read a line into s, return length */
int getline_p(char *s, int lim)
{
     char *start = s;
     char c;
     while (s < start + lim && (c = getchar()) != EOF && c != '\n')
	  *s++ = c;
     if (c == '\n')
	  *s = c;
     *++s = '\0';
     return s - start;
}
