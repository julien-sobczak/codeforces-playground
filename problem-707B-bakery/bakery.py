#!/usr/bin/env python3


(n, m, k) = map(int, input().split())

flours = []
distances = [input().split() for i in range(m)]

if k:
    flours = input().split()

answer = 10 ** 9
for d in distances:
    u = d[0]
    v = d[1]
    l = int(d[2])
    if (u in flours) ^ (v in flours):  
        answer = min(answer, l) 

print(answer if answer < 10 ** 9 else -1)         

    

