#include <stdio.h>
#define MAXVAL 100

int sp = 0;
double val[MAXVAL];

void push(double f)
{
     if (sp < MAXVAL)
	  val[sp++] = f;
     else
	  printf("Error: calc stack full, can't push %g\n", f);
}

double pop(void)
{
     if (sp > 0) {
	  return val[--sp];
     } else {
	  printf("Error: calc stack empty\n");
	  return 0.0;
     }
}
