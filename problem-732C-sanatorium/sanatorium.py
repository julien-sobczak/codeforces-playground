b, d, s = [int(n) for n in input().split()]

n = max(b, d, s) - 1

#print(n)
ans = max(n - b, 0) + max(n - d, 0) + max(n - s, 0)

print(ans)



