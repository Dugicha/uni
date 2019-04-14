// Author: Nikoloz Otiashvili
// K&R Exercise 3-6

#include <stdio.h>

void reverse(char s[], size_t len);
void itoa(int n, char s[], size_t p);

int main(void)
{
     char num[11];
     itoa(-69420, num, 10);
     printf("%s\n", num);
     return 0;
}

/* Reverses character string */
void reverse(char s[], size_t len)
{
     char temp;
     /* Swap equidistant characters from the middle */
     for (size_t i = 0; i < len/2; i++) {
	  temp = s[i];
	  s[i] = s[len - i - 1];
	  s[len - i - 1] = temp;
     }
}

/* Convert int to string and pads zeros until it reaches given length */
void itoa(int n, char s[], size_t p)
{
     int i = 0;
     short sign = (n < 0);	/* 1 - negative, 0 - positive  */

     /* Check if negative */
     if (sign) {
	  s[i++] = n % 10 + '0';
	  n /= -10;		/* Reduce and convert to positive */
     }

     while (n > 0) {
	  s[i++] = n % 10 + '0';
	  n /= 10;
     }

     /* Pad with 0s until min length reached */
     while (i < p) {
	  s[i++] = '0';
     }
     
     /* Add minus if negative */
     if (sign)
	  s[i++] = '-';
     
     s[i] = '\0';
     reverse(s, i);
}
