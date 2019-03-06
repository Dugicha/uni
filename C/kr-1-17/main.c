// Author: Nika Otiashvili
// K&R exercise 1-17

#include <stdio.h>
#define MAXCOUNT 1000 // Maximum lines
#define MAXCHAR 1000  // Maximum characters in a line
#define MINCHAR 80    // Minimum characters in a line for it to be valid

int get_line(char s[], int lim);
void copy(char to[], char from[]);

int main(void)
{
	 int len; // Current line length
	 char line[MAXCHAR]; // Current line content
	 char valid_lines[MAXCOUNT][MAXCHAR]; // All valid lines
	 int valid_line_count = 0; // Current valid line count

	 // Collect lines from input
	 while ((len = get_line(line, MAXCHAR)) > 0 && valid_line_count < MAXCOUNT)
		  if (len > MINCHAR) {
			   copy(valid_lines[valid_line_count], line);
			   ++valid_line_count;
		  }

	 // Print all valid lines (longer than 80 chars)
	 printf("\nLines longer than %i chars:\n", MINCHAR);
	 for (int i = 0; i < valid_line_count; ++i) {
		  len = printf("%s", valid_lines[i]);
		  // Print '\n' at the end of the line if missing
		  if (valid_lines[i][len-1] != '\n')
			   putchar('\n');
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
	 while ((to[i] = from[i]) != '\0')
		  ++i;
}
