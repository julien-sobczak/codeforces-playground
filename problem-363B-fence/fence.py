n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

m = sum(a[:k])
c = m
mi = k - 1

#print(a)
for ci in range(k, n): 
    c = c - a[ci - k] + a[ci]
    #print(ci, c)
    if c < m:
        m = c
        mi = ci

print(mi - k + 2)  # mi contains the 0-based index of the last element

