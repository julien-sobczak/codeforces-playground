#include <iostream>
using namespace std;

int main() 
{
    long n, a[500009], total;
    cin >> n;
    for (int i = 0; i < n; i++) 
    {
        cin >> a[i];
        total += a[i];
    }
    if (total % 3 != 0) {
        cout << 0 << endl;
        return 0;
    }
    long partial = total / 3;
    int c = 0;
    long s;
    int occurrences = 0;
    for (long i = 0; i < n - 1; i++) 
    {
        s += a[i];
        if (s == partial * 2) c += occurrences;
        if (s == partial) occurrences++;
    }
    cout << c << endl;
}
