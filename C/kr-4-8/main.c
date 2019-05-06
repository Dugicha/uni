// Author: Nikoloz Otiashvili
// K&R Exercise 4-8

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "calcstack.h"
#include "getop.h"

int main(void)
{
     int type;
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
	  case '\n':
	       printf("\t%.8g\n", pop());
	       break;
	  default:
	       printf("Error: unknown command %s\n", s);
	       break;
	  }
     }
     return 0;
}
