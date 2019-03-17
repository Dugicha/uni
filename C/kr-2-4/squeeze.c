// Author: Nika Otiashvili
// K&R exercise 2-4

#include <stdio.h>

void squeeze(char s1[], char s2[]);

int main(void)
{
     char test1[] = "cobalt";
     squeeze(test1, "asphalt");
     printf("squeeze(cobalt, asphalt) is %s\n", test1);

     char test2[] = "loremipsum";
     squeeze(test2, "texaslimit");
     printf("squeeze(loremipsum, texaslimit) is %s\n", test2);

     return 0;
}

/* Delete all chars from s1 that occur in s2 */
void squeeze(char s1[], char s2[])
{
     int copy_index = 0;
     for (int i = 0; s1[i] != '\0'; ++i) {

	  unsigned char occurrence_found = 0;

	  for (int j = 0; s2[j] != '\0'; ++j) {
	       if (s1[i] == s2[j]) {
		    occurrence_found = 1;
		    break;
	       }
	  }

	  if (occurrence_found == 0) {
	       s1[copy_index++] = s1[i];
	  }
     }
     s1[copy_index] = '\0';
}
