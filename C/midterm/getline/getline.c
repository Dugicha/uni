// Author: Nikoloz Otiashvili
// Midterm Var. 1, exercise 3

#include <stdio.h>
#define MAXLINE 1000

size_t getline_p(char *s, int lim);
int strindex_p(char *source, char *searchfor);

int main(int argc, char *argv[])
{
     char *pattern = argv[1];
     char line[MAXLINE];

     while (getline_p(line, MAXLINE) > 0)
	  if (strindex_p(line, pattern) == -1 ) {
	       printf("%s", line);
	  }

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

/* Read a line into s, return length */
size_t getline_p(char *s, int lim)
{
     char *start = s;
     while ((*s = getchar()) != EOF && *s++ != '\n')
	  ;

     *s = '\0';
     return s - start;
}

/* Copies from into to */
void copy(char *to, char *from)
{
     while ((*to++ = *from++))
	  ;
}

/* Reverses line in place */
void reverse(char *s, size_t len)
{
     char *last = s + len - 1;
     char temp;
     while (last - s >= 1) {
	  temp = *s;
	  *s++ = *last;
	  *last-- = temp;
     }
}
