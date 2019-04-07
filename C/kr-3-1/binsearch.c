// Author: Nika Otiashvili'
// K&R Exercise 3-1

#include <stdio.h>

int binsearch(int x, int v[], int n);

int main(void)
{
     int v[] = {4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49 };
     int x = 7;
     printf("binsearch(7, v, 15) = %i\n", binsearch(x, v, 15));

     return 0;
}

int binsearch(int x, int v[], int n)
{
     int low, mid, high;
     low = 0;
     high = n - 1;

     /* Don't search if element out of bounds */
     if (x < v[low] || x > v[high])
	  return -1;

     /* Removed equal comparison 'low <= high' */
     while (low < high) {
	  mid = (low + high) / 2;
	  if (x < v[mid])
	       high = mid - 1;
	  else if (x > v[mid])
	       low = mid + 1;
	  else			/* found match */
	       return mid;
     }

     /* When low == high  */
     if (x == v[low])
	  return low;

     return -1;			/* no match */
}
