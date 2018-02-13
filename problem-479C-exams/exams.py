n = int(input())
l = []
for i in range(n):
    exam = list(map(int, input().split()))
    l.append((exam[0], exam[1]))
l.sort()

c = 0
for exam in l:
     if exam[1] >= c:
         c = exam[1]
     else: 
         c = exam[0]


print(c)

