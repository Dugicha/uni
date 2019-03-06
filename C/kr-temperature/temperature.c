// Author: Nika Otiashvili
// K&R exercise 1-3 and 1-4
// Shows a table of temperatures from Celsisus to Fahrenheit

#include <stdio.h>

int main()
{
	 float fahr, cels;

	 int lower = 0;
	 int upper = 100;
	 int step = 10;
	 char* delimiter = "\t";

	 // Get widths of the words for formatting table
	 int celsius_width = printf("Celsius");
	 printf("%s", delimiter);
	 int fahrenheit_width = printf("Fahrenheit");
	 printf("\n");

	 cels = lower;
	 while (cels <= upper) {
		  fahr = cels * (9.0/5.0) + 32;
		  printf("%*.0f", celsius_width, cels);
		  printf("%s", delimiter);
		  printf("%*.1f", fahrenheit_width, fahr);
		  printf("\n");
		  cels += step;
	 }

	 return 0;
}
