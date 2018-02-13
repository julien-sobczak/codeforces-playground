n, k = map(int, input().split())
s = list(input())

start = 0
start1 = None
c = 0
p = s[0]

ans = 0

for i in range(1, n):
    l = s[i]
    print(i, "'", l, "'", start, start1)
    if l == p:
        continue
    if c < k:
       c += 1
       if c == 1:
           start1 = i
    else:
       if ans < i - start:
           ans = i - start
       start = start1
       c -= 1

if ans < n - start:
    ans = n - start

print(ans)
