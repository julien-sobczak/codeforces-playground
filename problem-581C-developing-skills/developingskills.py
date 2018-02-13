import math

n, k = map(int, input().split())
a = [int(i) for i in input().split()]

a.sort(reverse=True)


for i, ai in enumerate(a):
    if ai != 0 and ai % 10 == 0:
        continue
    p = int(ai / 10)
    r = (p + 1) * 10 - ai
    print(i, ":", ai, "+", r)
    if k >= r:
       a[i] += r
       k -= r
    if k < r:
        break 

for i, ai in enumerate(a):
    if k <= 0:
        break
    if ai < 100:
        b = min(100 - ai, k)
        k -= b
        a[i] += b
        print(i, ":", ai, "+", b)

ans = sum(int(ai / 10) for ai in a) 
print(ans)
