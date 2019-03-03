// Author: Nika Otiashvili
// K&R exercise 2-1

#include <stdio.h>
#include <math.h> /* for isinf */
#include <float.h>
#include <limits.h>

int main(void)
{
     unsigned char uc = 0;
     printf("unisgned char [0; %u]\n", --uc);
     printf("<limits.h>: unsigned char [0; %u]\n", UCHAR_MAX);

     unsigned short us = 0;
     printf("unsigned short [0; %u]\n", --us);
     printf("<limits.h>: unsigned short [0; %u]\n", USHRT_MAX);
     
     unsigned int ui = 0;
     printf("unsigned int [0; %u]\n", --ui);
     printf("<limits.h>: unsigned int [0; %u]\n", UINT_MAX);
     
     unsigned long ul = 0;
     printf("unsigned long [0; %lu]\n", --ul);
     printf("<limits.h>: unsigned long [0; %lu]\n", ULONG_MAX);
     
     signed char c = 2;
     while (c > 0)
	  c *= 2;
     printf("signed char [%d; ", c);
     c -= 1;
     printf("%d]\n", c);
     printf("<limits.h>: signed char [%d; %d]\n", SCHAR_MIN, SCHAR_MAX);

     signed short s = 2;
     while (s > 0)
	  s *= 2;
     printf("signed short [%d; ", s);
     s -= 1;
     printf("%d]\n", s);
     printf("<limits.h>: signed short [%d; %d]\n", SHRT_MIN, SHRT_MAX);
     
     signed int i = 2;
     while (i > 0)
	  i *= 2;
     printf("signed int [%d; ", i);
     i -= 1;
     printf("%d]\n", i);
     printf("<limits.h>: signed int [%d; %d]\n", INT_MIN, INT_MAX);
     
     signed long l = 2;
     while (l > 0)
	  l *= 2;
     printf("signed long [%ld; ", l);
     l -= 1;
     printf("%ld]\n", l );
     printf("<limits.h>: signed long [%ld; %ld]\n", LONG_MIN, LONG_MAX);

     // Print float limits
     float f = 1.0;
     while (!isinf((float) (f * 2.0)))
	  f *= 2.0;
     f = -f;
     printf("\nfloat [%f; ", f);
     f = -f;
     printf("%f]\n", f);
     printf("<float.h>: float [%f; %f]\n", FLT_MIN, FLT_MAX);
     
     // Print float precision
     float f2 = 1.0;
     int float_precision_count = 1;
     while ((float) (f2 / 2.0) != (float) 0.0) {
	  f2 /= 2.0;
	  float_precision_count += 1;
     }
     printf("float precision is %d\n", float_precision_count);
     printf("<float.h>: float precision is %d\n", FLT_DIG);
	  
     // Print double limits
     double d = 1.0;
     while (!isinf((double) (d * 2.0)))
	  d *= 2.0;
     d = -d;
     printf("\ndouble [%f; \n", d);
     d = -d;
     printf("%f]\n", d);
     printf("<float.h>: double [%f; %f]\n", DBL_MIN, DBL_MAX);
     
     // Print double precision
     double d2 = 1.0;
     int double_precision_count = 1;
     while ((double) (d2 / 2.0) != (double) 0.0) {
	  d2 /= 2.0;
	  double_precision_count += 1;
     }
     printf("double precision is %d\n", double_precision_count);
     printf("<float.h>: double precision is %d\n", DBL_DIG);

     return 0;
}
