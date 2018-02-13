from array import array

n = int(input())
s = list(input())

cR = 0
cD = 0

new_s = s

while len(set(new_s)) == 2: 
  s = new_s
  new_s = list()
  for c in s:

    if c == 'R': 
      if cR == 0: 
        new_s.append('R')
        cD += 1
      else:
        cR -= 1

    elif c == 'D':
      if cD == 0:
        new_s.append('D')
        cR += 1 
      else:
        cD -= 1 

print(new_s[0])

