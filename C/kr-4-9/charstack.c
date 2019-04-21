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
     if (bufp >= BUFSIZE) {
	  printf("ungetch: buffer full\n");
     } else {
	  if (c == EOF)
	       buf[bufp++] = '\n';
	  else
	       buf[bufp++] = c;
     }
}
