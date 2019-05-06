#include <stdio.h>

char buf;		     /* Buffer with size of 1 char */
int buf_empty = 1;	     /* Signifies if buf can be overwritten */

/* Pop last item in char buffer */
int getch(void)
{
     if (buf_empty) {
	  return getchar();
     } else {
	  buf_empty = 1;
	  return buf;
     }
}

/* Push item into char buffer */
void ungetch(int c)
{
     if (buf_empty) {
	  buf_empty = 0;
	  buf = c;
     } else {		/* According to exercise, will never happen */
	  printf("ungetch: buffer full\n");
     }
}
