n = int(input())
a = list(map(int, input().split()))
b = sorted(a)


for l in range(n):
    if a[l] != b[l]:
        break
if l == n - 1:
    print("yes")
    print("1 1")
    exit(0)
for r in range(n - 1, 0, -1):
    if a[r] != b[r]:
        break
for i in range(l, r + 1):
    j = r - (i - l)
    if a[i] != b[j]:
       print("no")
       exit(0)
print("yes")
print("%s %s" % (l + 1, r + 1))
