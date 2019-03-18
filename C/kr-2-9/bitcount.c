// Author: Nika Otiashvili
// K&R Exercise 2-9

#include <stdio.h>

unsigned bitcount(unsigned x);

int main(void)
{
     printf("bitcount(100) = %i\n", bitcount(100)); /* 3 */
     printf("bitcount(63) = %i\n", bitcount(63));   /* 6 */
     printf("bitcount(71) = %i\n", bitcount(71));   /* 4 */
     return 0;
}

unsigned bitcount(unsigned x)
{
     unsigned b = 0;
     while (x & ~0) {
	  x &= x - 1;
	  b++;
     }
     return b;
}
