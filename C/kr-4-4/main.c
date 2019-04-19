// Author: Nikoloz Otiashvili
// K&R Exercise 4-4

#include <stdio.h>
#include <stdlib.h>
#include "calcstack.h"
#include "getop.h"

int main(void)
{
     int type;
     double op2;
     char s[MAXOP];
     int print_on_newline = 1;
     
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
	  case 'p':		/* Print last number in stack */
	       printf("\t%.8g\n", get_last());
	       print_on_newline = 0;
	       break;
	  case 's':		/* Swap last two numbers */
	       op2 = pop();
	       double op1 = pop();
	       push(op2);
	       push(op1);
	       print_on_newline = 0;
	       break;
	  case 'c':		/* Clear the stack */
	       clear();
	       print_on_newline = 0;
	       break;
	  case '\n':
	       if (print_on_newline)
		    printf("\t%.8g\n", pop());
	       else
		    print_on_newline = 1;
	       break;
	  default:
	       printf("Error: unknown command %s\n", s);
	       break;
	  }
     }
     return 0;
}
