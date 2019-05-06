#include <stdio.h>
#define BUFSIZE 100

char buf[BUFSIZE];
size_t bufp = 0;

/* Pop last item in char buffer */
int getch(void)
{
     return (bufp > 0) ? buf[--bufp] : getchar();
}

/* Push item into char buffer */
void ungetch(int c)
{
     if (bufp >= BUFSIZE)
	  printf("ungetch: buffer full\n");
     else
	  buf[bufp++] = c;
}

/* Push string into char buffer. Has no access to buf and bufp.
   Will always try to push string into buf even if it cuts off */
void ungets(char s[])
{
     for (size_t i = 0; s[i] ; i++)
	  ungetch(s[i]);
     ungetch('\0');
}

/* Push string into char buffer safely. Has access to buf and bufp.
   Will not push string if there is no space in buf */
void ungetsafe(char s[])
{
     /* Get length of s */
     size_t len = 0;
     while(s[len])
	  len++;
     /* Push s into buf if it fits */
     if (len <= BUFSIZE - bufp) {
	  for (size_t i = 0; i < len; i++)
	       ungetch(s[i]);
	  ungetch('\0');
     } else {
	  printf("ungetsafe: buffer can't fit \"%s\"", s);
     }
}
