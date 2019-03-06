// Author: Nika Otiashvili
// K&R exercise 1-16

#include <stdio.h>
#define MAXLINE 10

int get_line(char s[], int lim);
void copy(char to[], char from[]);

int main(void)
{
	 int len; // Current line length up to MAXLINE
	 int last_len; // Length of the last read segment of current line
	 int max; // Max length so far
	 char line[MAXLINE]; // Current line content
	 char longest[MAXLINE]; // Longest line content so far
	 char starting_segment[MAXLINE]; // Starting segment of longest line so far

	 max = 0;
	 last_len = 0;
	 while ((len = get_line(line, MAXLINE)) > 0) {
		  if (last_len + len > max) {
			   max = last_len + len;
			   if (last_len) {
					copy(longest, starting_segment);
			   } else {
					copy(longest, line);
			   }
		  }

		  // If line ends with '\n' (automatically inserted by get_line)
		  // that means it's shorter than MAXLINE, so we reset last_len
		  if (line[len-1] == '\n') {
			   last_len = 0;
		  } else {
			   // If line doesn't end with '\n'
			   // we need to keep adding last_len to max
			   if (last_len == 0)
					copy(starting_segment, line);
			   last_len += len;
		  }
	 }

	 // If a at least one line was inputted
	 if (max > 0) {
		  printf("\nLongest line:\n%s\n", longest);
		  printf("Length: %i\n", max);
	 }

	 return 0;
}

// Reads a line into s, returns length
int get_line(char s[], int lim)
{
	 int c, i;

	 for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
		  s[i] = c;
	 if (c == '\n') {
		  s[i] = c;
		  ++i;
	 }
	 s[i] = '\0';
	 return i;
}

void copy(char to[], char from[])
{
	 int i;
	 i = 0;
	 while ((to[i] = from[i]) != '\0') {
		  ++i;
	 }
}
