// Author: Nikoloz Otiashvili
// Midterm Var. 1, exercise 1

#include <stdio.h>
#define MAXLINE 1000

size_t get_line(char *s, int lim);
void copy(char *to, char *from);
void reverse(char *s, size_t len);

int main(void)
{
     size_t len, max;
     char line[MAXLINE];
     char longest[MAXLINE];

     max = 0;
     while ((len = get_line(line, MAXLINE)) > 0)
	  if (len > max) {
	       max = len;
	       copy(longest, line);
	  }

     /* If a at least one line was input */
     if (max > 0) {
	  reverse(longest, max);
	  printf("\n%s", longest);
     }

     return 0;
}

/* Read a line into s, return length */
size_t get_line(char *s, int lim)
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
