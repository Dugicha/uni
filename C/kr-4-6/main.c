// Author: Nikoloz Otiashvili
// K&R Exercise 4-5

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "calcstack.h"
#include "getop.h"

int main(void)
{
     int type;
     int print_on_newline = 1;
     double vars['z' - 'a' + 1];
     double recently_printed;
     double op2;
     char s[MAXOP];

     while ((type = getop(s)) != EOF) {
	  switch (type) {
	  case NUMBER:
	       push(atof(s));
	       break;
	  case '+':
	       push(pop() + pop());
	       break;
	  case '-':
	       op2 = pop();
	       push(pop() - op2);
	       break;
	  case '*':
	       push(pop() * pop());
	       break;
	  case '/':
	       op2 = pop();
	       if (op2 != 0.0)
		    push(pop() / op2);
	       else
		    printf("Error: can't divide by zero\n");
	       break;
	  case '%':
	       op2 = pop();
	       push((int) pop() % (int) op2);
	       break;
	  case '$':		/* Print most recently printed number */
	       print_on_newline = 0; /* Prevent \n from printing last element in stack */
	       printf("\t%.8g\n", recently_printed);
	       break;
	  case '\n':
	       if (print_on_newline) {
		    recently_printed = pop();
		    printf("\t%.8g\n", recently_printed);
	       } else {
		    print_on_newline = 1;
	       }
	       break;
	  default:
	       /* Write number into vars */
	       if (type >= 'a' && type <= 'z')
		    vars['a' - type] = pop();
	       else
		    printf("Error: unknown command %s\n", s);
	       break;
	  }
     }
     return 0;
}
