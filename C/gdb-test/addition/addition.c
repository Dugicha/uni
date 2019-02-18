#include <stdio.h>

int sum(int a, int b);

int main()
{
	 int a = 5;
	 int b = 12;
	 printf("jami %d + %d = %d\n", a, b, sum(a, b));
			return 0;
}

int sum(int a, int b) {
	 return a + b;
}
