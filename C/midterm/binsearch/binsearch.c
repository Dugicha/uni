// Author: Nikoloz Otiashvili
// Midterm Var. 1, exercise 2

#include <stdio.h>

size_t binsearch(int x, int *v, int n);

int main(void)
{
     int v[] = {4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46};
     int x = 19;
     printf("binsearch(19, v, 15) = %li\n", binsearch(x, v, 15));

     return 0;
}

size_t binsearch(int x, int *v, int n)
{
     size_t low, mid, high;
     int subt = 0;
     low = 0;
     high = n - 1;

     while (low <= high) {
	  mid = (low + high)/2;
	  subt = ((x - *(v + mid)) < 0);
	  switch (subt) {
	  case 1:
	       high = mid - 1;
	       break;
	  case 0:
	       if (x == *(v + mid))
		    return mid;
	       low = mid + 1;
	       break;
	  default:
	       return mid;
	  }
     }
     return -1;
}
