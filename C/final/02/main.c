#include <stdio.h>

#define arrsize 10

void print_array(int array[], size_t size);

int main()
{
	 int list[arrsize] = {3, 9, 8, 7, 6, 5, 4, 10, 2, 1};

	 printf("starting array =");
	 print_array(list, arrsize);
	 int count = 0;
	 int marchcount = 0;

	 for (size_t i = 1; i < arrsize; i++) {
		  count++;
		  int newElement = list[i];
		  size_t location = i - 1;
		  while (location >= 0 && list[location] > newElement) {
			   count += 2;
			   marchcount++;
			   list[location + 1] = list[location];
			   location -= 1;
			   print_array(list, arrsize);
		  }
		  list[location + 1] = newElement;
	 }

	 printf("final array =\t");
	 print_array(list, arrsize);
	 printf("count %i\n", count);
	 printf("marchcount %i\n", marchcount);
	 return 0;
}

void print_array(int array[], size_t size) {
	 for (size_t i = 0; i < size-1; i++)
		  printf("%i,\t", array[i]);
	 printf("%i\n", array[size-1]);
}
