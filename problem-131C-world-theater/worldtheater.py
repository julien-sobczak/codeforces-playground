from math import factorial as fact

n, m, t = map(int, input().split())

a = 0

for i in range(4, t + 1):
  # choose i boys and t - i girls among n and m respectively
  if i < 4 or t - i < 1: 
    continue
  a1 = fact(n) // (fact(i) * fact(n - i)) 
  a2 = fact(m) // (fact(t - i) * fact(m - (t - i)))
  #print("a1=", a1, ", a2=", a2)
  a += a1 * a2

print(a)
