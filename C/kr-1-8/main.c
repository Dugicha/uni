#include "stdio.h"
// Author: Nikoloz Otiashvili
// Counts blanks, lines and tabs in input
int main(int argc, char* argv[]) {
  
  int c, blank_count, tab_count, line_count;
  
  while ((c = getchar()) != EOF) {
    if (c == ' ') {
      ++blank_count;
    } else if (c == '\t') {
      ++tab_count;
    } else if (c == '\n') {
      ++line_count;
    }
  }
  printf("\nBlank count: %i\n", blank_count);
  printf("Tab count: %i\n", tab_count);
  printf("Line count: %i\n", line_count);
  return 0;
}
