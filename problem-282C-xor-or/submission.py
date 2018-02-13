a = [int(a) for a in input()]
b = [int(b) for b in input()]

if len(a) != len(b):
  print("NO")
  exit(0)

possible = True

for i, ai in enumerate(a):
  if i == 0: 
    continue
  aip = a[i-1]
  bip = b[i-1]
  bi = b[i]
  if aip == bip and ai == bi:
    continue
  
  problem = True
  p = aip | ai
  q = aip ^ ai
  if p == bi: 
    if q == bip:
      a[i-1] = bip
      a[i] = bi
      problem = False
  if problem and p == bip:
    if q == bi:
      a[i-1] = bi
      a[i] = bip
      problem = False
 
  if problem:
    possible = False
    break
    

if possible:
  print("YES")
else:
  print("NO")

