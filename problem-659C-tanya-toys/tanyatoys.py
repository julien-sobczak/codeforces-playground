n, m = map(int, input().split())
a = set(map(int, input().split()))

t = []

for i in range(1, 10 ** 9 + 1):
    if i in a:
        # Already bought
        continue
    else:
        if m < i:
            # No nore money
            break
        else:
            t.append(i)
            m -= i

print(len(t))
print(*t)
