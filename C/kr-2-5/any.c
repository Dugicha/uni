// Author: Nika Otiashvili
// K&R exercise 2-5

#include <stdio.h>

int any(char s1[], char s2[]);

int main(void)
{
	 printf("any(cat, dog) is %i\n", any("cat", "dog"));
	 printf("any(lorem, man) is %i\n", any("lorem", "man"));
	 printf("any(yes, indeed) is %i\n", any("yes", "indeed"));
	 return 0;
}

/* Return location of first char in s1 that is also in s2 */
int any(char s1[], char s2[])
{
	 for (size_t i = 0; s1[i] != '\0'; ++i)
		  for (size_t j = 0; s2[j] != '\0'; ++j)
			   if (s1[i] == s2[j])
					return i;
	 return -1;
}
