#include <stdio.h>

#define arrsize 10

size_t find_largest(int v[], size_t size);
void swap(int *v, int i, int j);
void sort(int v[], size_t size, int sorted_array[]);

int main(void)
{
	 int array[arrsize] = { 3, 6, 9, 10, 1, 2, 5, 4, 8, 7 };
	 int sorted_array[arrsize] = {0};
	 sort(array, arrsize, sorted_array);
	 
	 // Print array
	 for (size_t i = 0; i < arrsize - 1; i++)
		  printf("%i, ", array[i]);
	 printf("%i\n", array[arrsize - 1]);
}

// Finds index of largest element in array up to given size
size_t find_largest(int v[], size_t size)
{
	 size_t l = 0; // Index of largest element
	 for (size_t i = 0; i < size; i++) {
		  if (v[l] < v[i])
			   l = i;
	 }
	 return l;
}

// Swaps v[i] and v[j]
void swap(int *v, int i, int j)
{
	 int temp;
	 temp = *(v + i);
	 *(v + i) = *(v + j);
	 *(v + j) = temp;
}

void sort(int v[], size_t size, int sorted_array[])
{
	 for (size_t i = 0; i < size; i++)
		  swap(v, size - 1 - i, find_largest(v, size - i));
}
