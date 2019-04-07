// Author: Nika Otiashvili'
// K&R Exercise 2-10

#include <stdio.h>

char lower_char(char c);
void lower(char s[]);

int main(void)
{
     char test1[] = "Lorem Ipsum 123";
     printf("lower(%s) = ", test1);
     lower(test1);
     printf("%s\n", test1);

     char test2[] = "tAkE OUT tHe TRash.";
     printf("lower(%s) = ", test2);
     lower(test2);
     printf("%s\n", test2);

     return 0;
}

 /* Converts one character to lowercase */
char lower_char(char c)
{
     return (c >= 'A' && c <= 'Z') ? (c - 'A' + 'a') : c;
}

/* Converts a string of characters to lowercase */
void lower(char s[])
{
     for (int i = 0; s[i] != '\0'; ++i)
	  s[i] = lower_char(s[i]);
}
