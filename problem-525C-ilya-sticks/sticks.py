n = int(input())
l = [int(i) for i in input().split()]

l.sort(reverse=True)

ans = 0
area = 0
ignore_next = False

for i in range(n - 1):
  if ignore_next:
    ignore_next = False
    continue

  l1 = l[i] 
  l2 = l[i+1]
  length = 0
  #print("compare", l1, l2)
  if l1 == l2:
    length = l1
  elif l1 == l2 + 1:
    length = l1 - 1
  #print('length=', length, ' area=', area)
  if length:
    if area:
      ans += area * length
      area = 0
    else:
      area = length
    ignore_next = True

print(ans)
