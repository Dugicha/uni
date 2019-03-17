// Author: Nika Otiashvili
// K&R exercise 2-7

#include <stdio.h>

unsigned invert(unsigned x, unsigned p, unsigned n);

int main(void)
{
     printf("invert(115, 3, 3) = %i\n", invert(115, 3, 3));
     printf("invert(63, 6, 4) = %i\n", invert(63, 6, 4));
     return 0;
}

unsigned invert(unsigned x, unsigned p, unsigned n)
{
     size_t len = sizeof(x) * 8 - 1;
     unsigned a = x >> p << p;
     unsigned b = (x << (len - (p - n))) >> (len - (p - n));
     unsigned c = ~(x << (len - p)) >> (len - p);
     return a | b | c;
}
