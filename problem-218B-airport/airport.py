from heapq import * 

n, m = map(int, input().split())
a = [] # Increasing order (least expensive to more expensive)
b = [] # 'False' decreasing order (most expensive to least expensive)
for ai in input().split():
  heappush(a, int(ai))
  heappush(b, n - int(ai))

pmin = 0
pmax = 0

for ni in range(n):
  ai = heappop(a)
  bi = heappop(b)
  #print('>', ai, (n - bi))
  pmin += ai
  pmax += (n - bi)
  if ai >= 2:
    heappush(a, ai - 1)
  if bi < n - 1:
    heappush(b, bi + 1)

print(pmax, pmin)

