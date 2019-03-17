// Author: Nika Otiashvili
// K&R exercise 2-6

#include <stdio.h>

unsigned setbits(unsigned x, unsigned p, unsigned n, unsigned y);

int main(void)
{
     printf("setbits(100, 4, 3, 71) = %i\n", setbits(100, 4, 3, 71));
     printf("setbits(69, 3, 2, 12) = %i\n", setbits(69, 3, 2, 12));
     printf("setbits(561, 7, 4, 63) = %i\n", setbits(561, 7, 4, 63));
     printf("setbits(165, 7, 3, 36) = %i\n", setbits(165, 7, 3, 36));
     return 0;
}

unsigned setbits(unsigned x, unsigned p, unsigned n, unsigned y)
{
     size_t len = sizeof(x) * 8 - 1;
     unsigned a = x >> (p + 1) << (p + 1);
     unsigned b = (x << (len - p + n)) >> (len - p + n);
     unsigned c = (y << (len - n)) >> (len - p - 1);
     return a | b | c;
}
