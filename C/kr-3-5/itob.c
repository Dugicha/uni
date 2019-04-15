// Author: Nikoloz Otiashvili
// K&R Exercise 3-5

#include <stdio.h>

void reverse(char s[], size_t len);
void itob(int n, char s[], int b);

int main(void)
{
     int num = 69420;
     char s[10];
     itob(num, s, 16);
     printf("%X %s\n", num, s);
     itob(num, s, 8);
     printf("%o %s\n", num, s);
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

/* Convert int to string and format to base b */
void itob(int n, char s[], int b)
{
     int i = 0;
     short sign = (n < 0);	/* 1 - negative, 0 - positive  */

     /* Check if negative */
     if (sign) {
	  int unit = n % b;
	  if (unit > 9)
	       s[i++] = 'A' + unit - 10;
	  else
	       s[i++] = '0' + unit;
	  n /= -b;		/* Reduce and convert to positive */
     }

     while (n > 0) {
	  int unit = n % b;
	  if (unit > 9)
	       s[i++] = 'A' + unit - 10;
	  else
	       s[i++] = '0' + unit;
	  n /= b;
     }

     /* Add minus if negative */
     if (sign)
	  s[i++] = '-';
     
     s[i] = '\0';
     reverse(s, i);
}
