// Author: Nikoloz Otiashvili
// K&R Exercise 3-3

#include <stdio.h>

short is_valid_expression(char a, char dash, char b);
void expand(char s1[], char s2[]);

int main(void)
{
     char s2[100];
     expand("Should expand: a-b a-k-z\nShould not expand: b-a 9-5 A-9", s2);
     printf("%s\n", s2);
     printf("--b-4-6-9-z-A-J-z should expand into:\n --b-456789-z-ABCDEFGHIJ-z\n");
     expand("It expands into:\n --b-4-6-9-z-A-J-z", s2);
     printf("%s\n", s2);

     return 0;
}

/* Evaluates if the dash expression is valid */
short is_valid_expression(char a, char dash, char b)
{
     if (dash != '-')
	  return 0;
     
     if (a >= '0' && a <= '9')
	  return b > a && b <= '9';
     else if (a >= 'a' && a <= 'z')
	  return b > a && b <= 'z';
     else if (a >= 'A' && a <= 'Z')
	  return b > a && b <= 'Z';
     else
	  return 0;
}

/* Copy chars from from[] into to[] while expanding dash expressions */
void expand(char from[], char to[])
{
     int j = 0; /* Current index of to[] */

     for (int i = 0; from[i] != '\0'; i++) {
	  if (from[i+1] == '-' && is_valid_expression(from[i], from[i+1], from[i+2])) {
	       do {
		    /* Expand characters */
		    for (char c = from[i]; c < from[i+2]; c++)
			 to[j++] = c;
		    /* Move to next expression (if chained) */
		    i += 2;
	       } while (is_valid_expression(from[i], from[i+1], from[i+2]));
	       to[j++] = from[i];
	  } else {
	       to[j++] = from[i];	    
	  }
     }
     to[j] = '\0';
}
