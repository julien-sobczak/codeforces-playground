#include <iostream>
#include <math.h>
using namespace std;

int main ()
{
  int n, m, a;
  cin >> n >> m >> a;
  int s_width = ceil(n * 1.0 / a);
  int s_height = ceil(m * 1.0 / a);
  int s = s_width * s_height;
  cout << s << "\n";
  return 0;
}
