// Author: Nikoloz Otiashvili
// Verifies whether getchar() != EOF is 0 or 1

#include <stdio.h>

int main()
{
	 while((getchar() != EOF) == 0)
		  printf("Not EOF\n");
	 printf("EOF\n");
}
