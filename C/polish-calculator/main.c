/* R&K Reverse Polish Calculator 82:96 */

#include <stdio.h>
#include "calc.h"
#include <stdlib.h> /* for atof() */
#define MAXOP 100 /* max size of operand or operator */

int main()
{
    int type;
    double op2;
    char s[MAXOP];

    while ((type = getop(s)) != EOF) 
    {
        switch(type)
        {
            case NUMBER:
                push(atof(s));
                break;
            case  '+':  // 0x2b
                push(pop() + pop());                
                break;
            case  '-':  // 0x2d
                op2 = pop();
                push(pop() - op2);
                break;
            case  '*':  // 0x2a
                push(pop() * pop());
                break;
            case  '/':  // 0x2f
                op2 = pop();
                if(op2 != 0.0)
                    push(pop() / op2);
                else                    
                printf("Error: zero divisor.\n");
                break;
            case  '\n':  // 
                printf("\t%.8g\n", pop());
                break;            
            default :
                printf("Error: unknown command %s.\n", s);
        }
    }
    
    return 0;  
}















