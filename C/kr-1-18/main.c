// Author: Nika Otiashvili
// K&R exercise 1-18

#include <stdio.h>
#define MAXCOUNT 1000 // Maximum lines
#define MAXCHAR 1000  // Maximum characters in a line

void trim(char line[], int len);
int get_line(char s[], int lim);
void copy(char to[], char from[]);

int main(void)
{
	 int len; // Current line length
	 char line[MAXCHAR]; // Current line content
	 char trimmed_lines[MAXCOUNT][MAXCHAR]; // All trimmed lines
	 int line_count = 0;

	 // Collect lines from input
	 while ((len = get_line(line, MAXCHAR)) > 0 && line_count < MAXCOUNT) {
		  trim(line, len);
		  copy(trimmed_lines[line_count], line);
		  ++line_count;
	 }

	 // Print trimmed lines (with removed trailing whitespace)
	 printf("\nTrimmed lines:\n");
	 for (int i = 0; i < line_count; ++i) {
		  len = printf("%s", trimmed_lines[i]);
		  // Print '\n' at the end of non-empty line where it's missing
		  if (len != 0 && trimmed_lines[i][len-1] != '\n') {
			   putchar('\n');
		  }
	 }

	 return 0;
}

// Removes trailing whitespace from line
void trim(char line[], int len)
{
	 int offset = 0;
	 // Determine offset (to move every char down)
	 for (int i = 0; i < len; ++i)
		  if (line[i] == '\t' || line[i] == ' ' || line[i] == '\n')
			   offset = i + 1;
		  else
			   break;

	 // Copy chars down with offset
	 for (int i = offset; i < len; ++i)
		  line[i - offset] = line[i];

	 // Add null at the new end of the line
	 line[len - offset] = '\0';
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
