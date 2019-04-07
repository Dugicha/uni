// Author: Nika Otiashvili
// K&R Exercise 3-2

#include <stdio.h>

void escape(char to[], char from[]);
void unescape(char to[], char from[]);

int main(void)
{
     char sample_text[] = "You need to vibrate\thigher\t so you can open the portal that \
connects\nthis world of \t3 D\t to one of \t\t4 D\t or \t\t\t5\tD\n";

     printf("The text:\n");
     printf("%s\n", sample_text);

     printf("When escaped is:\n");
     char escaped_text[131] = "";
     escape(escaped_text, sample_text);
     printf("%s\n", escaped_text);

     printf("\nWhen unescaped is:\n");
     char unescaped_text[131] = "";
     unescape(unescaped_text, escaped_text);
     printf("%s", unescaped_text);
     return 0;
}

void escape(char to[], char from[])
{
     size_t i = 0;
     size_t j = 0;
     while (from[i] != '\0') {
	  switch (from[i]) {
	  case '\n':
	       to[j++] = '\\';
	       to[j++] = 'n';
	       break;
	  case '\t':
	       to[j++] = '\\';
	       to[j++] = 't';
	       break;
	  case '\r':
	       to[j++] = '\\';
	       to[j++] = 'r';
	       break;
	  case '\a':
	       to[j++] = '\\';
	       to[j++] = 'a';
	       break;
	  case '\b':
	       to[j++] = '\\';
	       to[j++] = 'b';
	       break;
	  default:
	       to[j++] = from[i];
	       break;
	  }
	  i++;
     }
     to[j] = '\0';
}

void unescape(char to[], char from[])
{
     size_t i = 0;
     size_t j = 0;
     while (from[i] != '\0') {
	  if (from[i] == '\\' && from[i+1] != '\0') {
	       switch (from[i+1]) {
	       case 'n':
		    to[j++] = '\n';
		    break;
	       case 't':
		    to[j++] = '\t';
		    break;
	       case 'r':
		    to[j++] = '\r';
		    break;
	       case 'a':
		    to[j++] = '\a';
		    break;
	       case 'b':
		    to[j++] = '\b';
		    break;
	       default:
		    to[j++] = from[i];
		    break;
	       }
	       i++;
	  } else {
	       to[j++] = from[i];       
	  }
	  i++;
     }
     to[j] = '\0';
}
