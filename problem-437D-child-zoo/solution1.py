read = lambda: map(int, input().split())
n, m = read()
v = list(read())

e = []
for i in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    e.append((x, y, min(v[x], v[y])))
e.sort(key = lambda x: x[2], reverse = True)

belong = list(range(n))
union = [[i] for i in belong]
size = [1] * n

ans = 0

for i, j, k in e:
    print("New iteration with (%d, %d) -> %d" % (i, j, k))
    print("belong", belong)
    print("union", union)
    print("size", size)
    fi, fj = belong[i], belong[j];
    if fi == fj: continue
    if not (len(union[fi]) > len(union[fj])):
        fi, fj = fj, fi
    ans += k * size[fi] * size[fj]
    size[fi] += size[fj]
    union[fi] += union[fj]
    for t in union[fj]: belong[t] = fi
    print("                     ")
    print("belong", belong)
    print("union", union)
    print("size", size)
    print("-----------------")
    
print("%.7lf" % (ans * 2 / n / (n - 1)))
