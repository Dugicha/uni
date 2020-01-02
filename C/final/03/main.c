#include <stdio.h>

#define arrsize 10

void swap(int *v, int i, int j);
void qsort(int *v, int left, int right);

int main(void)
{
	 int array[arrsize] = { 3, 6, 9, 10, 1, 2, 5, 4, 8, 7 };
	 qsort(array, 0, arrsize - 1);

	 // Print array
	 for (size_t i = 0; i < arrsize - 1; i++)
		  printf("%i, ", *(array + i));
	 printf("%i\n", *(array + arrsize - 1));
}

void qsort(int *v, int left, int right)
{
	 int i, last;

	 if (left >= right)
		  return;

	 swap(v, left, (left/2 + right/2));
	 last = left;
	 for (i = left + 1; i <= right; i++)
		  if (*(v + i) < *(v + left))
			   swap(v, ++last, i);

	 swap(v, left, last);
	 qsort(v, left, last-1);
	 qsort(v, last+1, right);
}

void swap(int *v, int i, int j)
{
	 int temp;
	 temp = *(v + i);
	 *(v + i) = *(v + j);
	 *(v + j) = temp;
}
