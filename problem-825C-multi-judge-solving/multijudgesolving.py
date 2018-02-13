n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] <= k * 2:
    print(0)
    exit(0)

ans = 0
d = k * 2
for ai in a: 
    while ai > d:
        # Problem too difficult. Need to pass another one before
        d *= 2
        ans += 1
    if ai * 2 > d:
        d = ai * 2
   
print(ans) 
