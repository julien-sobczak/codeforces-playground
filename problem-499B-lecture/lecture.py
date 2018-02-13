n, m = map(int, input().split())
d = {}
for i in range(m):
    w1, w2 = input().split()
    l1 = len(w1)
    l2 = len(w2)
    if l1 <= l2:
        d[w1] = w1
        d[w2] = w1
    else:
        d[w1] = w2
        d[w2] = w2

a = []
for s in input().strip().split():
    a.append(d[s])

print(' '.join(a))

