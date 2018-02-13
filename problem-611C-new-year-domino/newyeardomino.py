from functools import lru_cache
import math

illegals = set()

@lru_cache(maxsize=100000)
def solve(r1, c1, r2, c2):
    print("solve(%d,%d,%d,%d)" % (r1, c1, r2, c2))
    w = c2 - c1 + 1
    h = r2 - r1 + 1

    if h < 1 or w < 1 or (h == 1 and w == 1):
        return 0

    ans = 0
    if h <= 2 and w <= 2:
        if h == 1:
            if (r1, c1) not in illegals and (r1 + 1, c1) not in illegals:
                ans += 1
        elif w == 1:
            if (r1, c1) not in illegals and (r1, c1 + 1) not in illegals:
                ans += 1
        else:  # h == 2 and w == 2 
            if (r1, c1) not in illegals and (r1 + 1, c1) not in illegals:
                ans += 1
            if (r1, c1 + 1) not in illegals and (r1 + 1, c1 + 1) not in illegals:
                ans += 1
            if (r1, c1) not in illegals and (r1, c1 + 1) not in illegals:
                ans += 1
            if (r1 + 1, c1) not in illegals and (r1 + 1, c1 + 1) not in illegals:
                ans += 1
    else:
        #print("Recurse because h=%s, w=%s" % (h, w))
        rsplit = math.floor(r1 + h / 2) 
        csplit = math.floor(c1 + w / 2)
        #print("new_r=%d, new_c=%d" % (rsplit, csplit))
        ans += solve(r1, c1, rsplit, csplit)
        ans += solve(r1, csplit, rsplit, c2)
        ans += solve(rsplit, c1, r2, csplit)
        ans += solve(rsplit, csplit, r2, c2)       
        
    return ans

h, w = map(int, input().split())
for i in range(h):
    points = list(input())
    illegals = illegals | set((i, j) for j, p in enumerate(points) if p == '#')
q = int(input())
for qi in range(q):
    r1, c1, r2, c2 = list(map(int, input().split()))
    print(solve(r1 - 1, c1 - 1, r2 - 1, c2 -1))

print('============')
print(illegals)

