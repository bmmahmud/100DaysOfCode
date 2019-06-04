/* Sum and Difference of Two Numbers*/
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int a, b;
  float x, y;
  scanf("%d %d", &a, &b);
  scanf("%f %f", &x, &y);
  printf("%d %d\n",( a + b),(a- b));
  printf("%.1f %.1f", (x + y), (x - y));

  return 0;
}
