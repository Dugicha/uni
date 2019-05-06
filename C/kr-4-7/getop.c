#include <stdio.h>
#include <ctype.h>
#include "charstack.h"
#include "getop.h"

/* Gets next operator or number */
int getop(char s[])
{
     int i, c;

     /* Skip all whitespace */
     while ((s[0] = c = getch()) == ' ' || c =='\t')
	  ;

     /* Terminate s in case it only has one character */
     s[1] = '\0';

     /* Operation */
     if (!isdigit(c) && c != '.' && c != '-')
	  return c;
     i = 0;

     /* Use '-' as operation if not followed by number */
     if (c == '-') {
	  c = getch();
	  ungetch(c);
	  if (!isdigit(c))
	       return '-';
     }

     /* Push integer part into s */
     if (isdigit(c))
	  while (isdigit(s[++i] = c = getch()))
	       ;
     /* Push fraction part into s */
     if (c == '.')
	  while (isdigit(s[++i] = c = getch()))
	       ;
     /* Terminate s */
     s[i] = '\0';

     /* If anything new shows up, push into char buffer */
     if (c != EOF)
	  ungetch(c);

     return NUMBER;
}
