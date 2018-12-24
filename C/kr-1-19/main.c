// Author: Nika Otiashvili
// K&R exercise 1-19

#include <stdio.h>
#define MAXCOUNT 1000 // Maximum lines
#define MAXCHAR 1000  // Maximum characters in a line

void reverse(char s[], int len);
int get_line(char s[], int lim);
void copy(char to[], char from[]);

int main(void) {
  int len; // Current line length
  char line[MAXCHAR]; // Current line content

  while ((len = get_line(line, MAXCHAR)) > 0) {
    // Remove '\n' if present at end of line
    if (line[len - 1] == '\n') {
      line [len - 1] = '\0';
      len = len - 1;
    }
    reverse(line, len);
    printf("%s\n", line);
  }

  return 0;
}

// Reverses character string
void reverse(char s[], int len) {
  char temp;
  // Exchange first and last characters, only need to do it len/2 times
  for (int i = 0; i < len / 2 + len % 2; ++i) {
    temp = s[i];
    s[i] = s[len - 1 - i];
    s[len - 1 - i] = temp;
  }
}

// Reverses character string without length argument
void rev(char s[]) {
  // Determine string length
  int len = 0;
  while (s[len] != '\0') {
    ++len;
  }
  // After this, the same as reverse function
  char temp;
  // Exchange first and last characters, only need to do it len/2 times
  for (int i = 0; i < len / 2 + len % 2; ++i) {
    temp = s[i];
    s[i] = s[len - 1 - i];
    s[len - 1 - i] = temp;
  }
}

// Reads a line into s, returns length
int get_line(char s[], int lim) {
  int c, i;

  for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i) {
    s[i] = c;
  }
  if (c == '\n') {
    s[i] = c;
    ++i;
  }
  s[i] = '\0';
  return i;
}

void copy(char to[], char from[]) {
  int i;
  i = 0;
  while ((to[i] = from[i]) != '\0') {
    ++i;
  }
}
