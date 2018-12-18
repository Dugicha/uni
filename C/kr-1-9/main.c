#include "stdio.h"
// Author: Nikoloz Otiashvili
// Squashes multiple blanks into one
int main(void) {
  int c;
  int previous_char_blank = 0;
  
  while ((c = getchar()) != EOF) {
    if (c != ' ') {
      putchar(c);
      previous_char_blank = 0;
    } else if (previous_char_blank == 0) {
      putchar(c);
      previous_char_blank = 1;
    }
  }
  
  return 0;
}
