// Author: Nikoloz Otiashvili
// K&R Exercise 4-1

#include <stdio.h>

int strrindex(char s[], char t);

int main(void)
{
     char test_string[] = "It is but a scratch!";
     char test_char_0 = 't';
     printf("strrindex(\"%s\", \'%c\') = %i\n", test_string, test_char_0,
	    strrindex(test_string, test_char_0));
     
     char test_char_1 = 'i';
     printf("strrindex(\"%s\", \'%c\') = %i\n", test_string, test_char_1,
	    strrindex(test_string, test_char_1));
     
     char test_char_2 = 'k';
     printf("strrindex(\"%s\", \'%c\') = %i\n", test_string, test_char_2,
	    strrindex(test_string, test_char_2));
     
     return 0;
}

int strrindex(char s[], char t)
{
     int pos = -1;
     for (size_t i = 0; s[i] != '\0'; i++) {
	  if (s[i] == t)
	       pos = i;
     }
     return pos;
}
