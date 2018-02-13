n, m, k = map(int, input().split())
players = [int(input()) for i in range(m)]
fedor = int(input())

c = 0
for p in players:
    if bin(p ^ fedor).count("1") <= k:
        c += 1

print(c)
   
