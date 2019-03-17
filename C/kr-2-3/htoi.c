// Author: Nika Otiashvili
// K&R exercise 2-3

#include <stdio.h>
#include <unistd.h>

int htoi(char *hex);
int htoi_single(char hex_digit);
int power(int num, int amount);

/* Reads arguments passed to this program and runs htoi on it */
int main(int argc, char *argv[])
{
     if (argc < 2) {
	  printf("Argument missing\n");
	  return 1;
     }

     printf("%i\n", htoi(argv[1]));
     return 0;
}

/* Converts hexadecimal string of characters to decimal integer */
int htoi(char *hex)
{
     int len = 0;
     char c;
     while ((c = hex[len]) != '\0')
	  ++len;

     // Set start at index 2 if 0x or 0X included
     int start = 0;
     if (len > 0 && (hex[1] == 'x' || hex[1] == 'X'))
	  start = 2;

     int ans = 0;
     for (int i = start; i < len; ++i) {
	  ans += htoi_single(hex[i]) * power(16, len - i - 1);
     }

     return ans;
}

/* Converts single hexadecimal character to decimal integer */
int htoi_single(char hex_digit)
{
     if (hex_digit >= '0' && hex_digit <= '9')
	  return hex_digit - '0';
     else if (hex_digit >= 'a' && hex_digit <= 'f')
	  return 10 + hex_digit - 'a';
     else
	  return 10 + hex_digit - 'A';
}

/* Returns `num` to the power of `amount` */
int power(int num, int amount)
{
     int ans = 1;
     while (amount > 0) {
	  ans *= num;
	  amount -= 1;
     }
     return ans;
}
