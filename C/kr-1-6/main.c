#include <stdio.h>

// Verifies whether getchar() != EOF is 0 or 1
int main() {
  while((getchar() != EOF) == 0) {
    printf("Not EOF\n");
  }
  printf("EOF\n");
}
