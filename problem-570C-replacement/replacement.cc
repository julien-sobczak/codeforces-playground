#include <iostream>
#include <string>
#include <math.h>
#include <ctype.h>
#include <stdio.h>
using namespace std;

int main()
{
  int n, m;
  int x;
  int a;
  char c;
  char str[300000];
  scanf("%d %d", &n, &m);
  scanf("%s", str);
  for (int i = 0; i < m; i++) {
    scanf("%d %c", &x, &c);
    str[x - 1] = c;
    a = 0;
    for (int j = 1; j < n; j++) {
      if (str[j-1] == '.' && str[j] == '.') {
        a++;
      } 
    } 
    cout << a << endl;
  }
  return 0;
}

