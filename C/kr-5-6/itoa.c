// Author: Nikoloz Otiashvili
// K&R Exercise 5-6 (itoa, reverse)

#include <stdio.h>

void reverse_p(char *s, size_t len);
void itoa_p(int n, char *s);

int main(void)
{
     char num[10];
     itoa_p(-69420, num);
     printf("%s\n", num);
     return 0;
}

/* Reverses character string using pointers */
void reverse_p(char *s, size_t len)
{
     char temp;
     char *last = s + len - 1;
     /* Swap equidistant characters from the middle */
     while (last - s > 0) {
     	  temp = *s;
     	  *s++ = *last;
     	  *last-- = temp;
     }
}

/* Converts int to string */
void itoa_p(int n, char *s)
{
     char *start = s;
     short sign = (n < 0);	/* 1 - negative, 0 - positive  */

     /* Check if negative */
     if (sign) {
	  *s++ = n % 10 + '0';
	  n /= -10;		/* Reduce and convert to positive */
     }

     while (n > 0) {
	  *s++ = n % 10 + '0';
	  n /= 10;
     }

     /* Add minus if negative */
     if (sign)
	  *s++ = '-';
     
     *s = '\0';
     reverse_p(start, s - start);
}
