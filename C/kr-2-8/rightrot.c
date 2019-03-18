// Author: Nika Otiashvili
// K&R exercise 2-8

#include <stdio.h>

unsigned rightrot(unsigned x, unsigned n);

// #NOTE: make sure to rotate by n%32 to avoid overflows

int main(void)
{
     printf("rightrot(100, 3) = %i\n", rightrot(100, 3));
     printf("rightrot(96, 3) = %i\n", rightrot(96, 3));
     printf("rightrot(63, 31) = %i\n", rightrot(63, 31));
     printf("rightrot(4, 60) = %i\n", rightrot(4, 60));
     return 0;
}

unsigned rightrot(unsigned x, unsigned n)
{
     unsigned len = sizeof(x) * 8 - 1;
     n = n % (len + 1); /* Avoids overshifting */
     unsigned ans = 0;
     for (unsigned i = 0; i < n; ++i)
	  ans |= (x & (1 << i)) << (len - n);
     ans |= x >> 3;
     return ans;
}
