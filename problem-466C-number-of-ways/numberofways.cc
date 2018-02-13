#include <iostream>
using namespace std;

int main() 
{
    long n, a[500009], s;
    cin >> n;
    for (int i = 0; i < n; i++) 
    {
        cin >> a[i];
        s += a[i];
    }
    if (s % 3 != 0) {
        cout << 0 << endl;
        return 0;
    }
    int c = 0;
    long s1 = a[0];
    long s2 = 0;
    long s3 = 0;
    for (long i = 1; i < n - 1; i++) 
    {
        s2 = a[i];
 
        for (long j = i + 1; j < n; j++) 
        {
            //cout << "post(" << i << "," << j << ") " << s1 << s2 << (s - s1 - s2) << endl;
            if (s1 == s2 && s1 == s - s1 - s2) 
            {
                c++;
            }
            s2 += a[j];
        }

        s1 += a[i];
    }
    cout << c << endl;
}
