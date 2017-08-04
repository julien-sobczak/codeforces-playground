#include <iostream>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stdio.h>
using namespace std;

int main()
{
  int n, c, i;
  char colors[50], cur;
  scanf("%d", &n);
  scanf("%s", colors);

  cur = colors[0];
  for (c = 0, i = 1; i < n; i++) 
  {
    if (colors[i] == cur) c++;
    else cur = colors[i];
  }

  cout << c << endl;
}
