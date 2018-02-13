n, m = map(int, input().split())
v = { i+1: int(v) for i, v in enumerate(input().split())}

ans = 0
for i in range(m):
    x, y = map(int, input().split())
    ans += min(v[x], v[y])

print(ans)

