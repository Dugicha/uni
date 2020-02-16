// Author: Nika Otiashvili
// K&R exercise 4-14
// Defines swap macro that switches arguments with given type

#include <stdio.h>

#define printi(i) printf(#i " = %i\n", i)
#define prints(s) printf(#s " = %s\n", s)
#define swap(t,x,y) { t tmp = x; x = y; y = tmp; }

int main(void)
{
    int a = 12;
    int b = 13;
    char *c = "hello";
    char *d = "nyellow";
    printi(a);
    printi(b);
    prints(c);
    prints(d);
    swap(int, a, b);
    swap(char*, c, d);
    printi(a);
    printi(b);
    prints(c);
    prints(d);
}
