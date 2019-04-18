// Author: Nikoloz Otiashvili
// K&R Exercise 5-3

#include <stdio.h>

void strcat(char *s, char *t);

int main(void)
{
     char s[100] = "This is a sente";
     char t[] = "nce which ends.";
     strcat(s, t);
     printf("%s\n", s);
     
     return 0;
}

/* Copy t to the end of s; Pointer version */
void strcat(char *s, char *t)
{
     size_t i = 0;
     size_t j = 0;

     while (*(s+i))
	  i++;
     while (*(s + (i++)) = *(t + j))
	  j++;
}
