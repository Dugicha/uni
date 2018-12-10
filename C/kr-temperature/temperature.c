#include <stdio.h>

/* 
   Shows a table of temperatures from Celsisus to Fahrenheit
   k&r ex.1-3, 1-4
*/

int main() {
  float fahr, cels;
  int lower, upper, step;
  char* delimiter;

  lower = 0;
  upper = 100;
  step = 10;
  delimiter = "\t";
  
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
