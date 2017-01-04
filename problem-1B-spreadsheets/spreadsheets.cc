#include <iostream>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stdio.h>
using namespace std;

void letter(int number) {
  if (number) {
    letter((number - 1) / 26);
    putchar('A' + ((number - 1) % 26));
  }
}

int main()
{
  int n;
  int r, c;
  char str[20], *p;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%s", str);

    if (sscanf(str, "%*c%d%*c%d", &r, &c) == 2) { // Ex: R23C55
      letter(c);
      printf("%d\n", r);
    } else { // Ex: BC23
      for (c=0, p=str; *p >= 'A'; ++p) 
        c = c*26 + *p - 'A' + 1;
      printf("R%sC%d\n", p, c);
    }
  }
  return 0;
}
