import math

n, m = [int(d) for d in input().split()]

if n > m + 1 or (n + 1) * 2 < m: 
    print(-1)

elif n > m:
    print('01' * m + '0')    

elif m > n * 2:
    print('110' * n + '1' * (m - n * 2))

else:
    print('110' * (m - n) + '10' * (n * 2 - m))

