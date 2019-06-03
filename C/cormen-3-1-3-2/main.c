#include <stdio.h>

#define arrsize 9

void print_array(int array[], size_t size);

int main()
{
	 int list[arrsize] = {3, 5, 2, 9, 8, 1, 6, 4, 7};

	 printf("starting array = ");
	 print_array(list, arrsize);

	 for (size_t i = 1; i < arrsize; i++) {
		  int newElement = list[i];
		  size_t location = i - 1;
		  while (location >= 0 && list[location] > newElement) {
			   list[location + 1] = list[location];
			   location = location - 1;
		  }
		  printf("i = %lu, array = ", i);
		  print_array(list, arrsize);
		  list[location + 1] = newElement;
	 }

	 printf("final array = ");
	 print_array(list, arrsize);

	 return 0;
}

void print_array(int array[], size_t size) {
	 for (size_t i = 0; i < size-1; i++)
		  printf("%i, ", array[i]);
	 printf("%i\n", array[size-1]);
}
