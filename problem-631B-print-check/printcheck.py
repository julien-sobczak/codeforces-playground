n, m, k = map(int, input().split())

r = [[0 for x in range(m)] for y in range(n)] 

for i in range(k):
  t, rc, a = map(int, input().split())
  if t == 1:
    for j in range(m):
      r[rc - 1][j] = a
  else:
    for j in range(n):
      r[j][rc - 1] = a

for i in range(n):
  print(*r[i])
