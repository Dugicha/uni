// Author: Nikoloz Otiashvili
// K&R Exercise 5-5

#include <stdio.h>

void strncat(char *s, char *t, size_t n);
void strncpy(char s[], char t[], size_t n);

int main(void)
{
     char s[100] = "This is a sente";
     char t[] = "nce which ends.";
     strncat(s, t, 3);
     printf("%s\n", s);

     char s2[100] = "This is replaced, but this is left";
     char t2[] = "This one is right, but not this";
     strncpy(s2, t2, 17);
     printf("%s\n", s2);
     
     return 0;
}

/* Copy n characters from t to the end of s */
void strncat(char *s, char *t, size_t n)
{
     /* Get pointer for the last character in s */
     size_t i = 0;
     while (s[i])
	  i++;
     /* Copy until end or until n runs out */
     for (size_t j = 0; (s[i++] = t[j++]) && n > 0; n--)
	  ;
}

/* Copy at most n characters from t to s */
void strncpy(char s[], char t[], size_t n)
{
     /* Copy from t until t ends or i reaches n */
     for (size_t i = 0; t[i] && i < n; i++)
	  s[i] = t[i];
}
