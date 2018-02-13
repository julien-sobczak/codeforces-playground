n, m = map(int, input().split())
a = [int(a) for a in input().split()]
d = {}

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if y not in d:
        d[y] = set()
    if x not in d:
        d[x] = set()
    if x < y:
        t = (x, y)
        d[y].add(t)
    else:
        t = (y, x)
        d[x].add(t)

def fp(x, y):
    print("fp(%d, %d)" % (x, y))
    if not d.get(y):
        return None
   
    min_res = 10 ** 5
    print(d[y])
    for t in d[y]:
        print(t)
        if t[0] == x:
            new_res = min(a[x], a[y])
        else:  # recurse
            new_res = fp(x, t[0])
            if new_res:
                new_res = min(new_res, a[y])
            else:
                continue
        if new_res and new_res < min_res:
            min_res = new_res

    return min_res

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        res = fp(i, j)
        if res:
            ans += res
            
ans /= n * (n - 1)

print(ans)
