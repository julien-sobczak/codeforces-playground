n = int(input())
n1, *c1 = list(map(int, input().split()))
n2, *c2 = list(map(int, input().split()))

from collections import deque

q1 = deque(c1)
q2 = deque(c2)

count = 0
while len(q1) > 0 and len(q2) > 0:
    count += 1
    
    # Break if too many iterations
    if count > 99999:
        print("-1")
        exit(0)
  
    i1 = q1.popleft()
    i2 = q2.popleft()
 
    #print("Battle %s vs %s" % (i1, i2))

    if i1 > i2:
        q1.append(i2)
        q1.append(i1) 
    else:
        q2.append(i1)
        q2.append(i2) 


if len(q1):
    print("%d 1" % count)
else:
    print("%d 2" % count)
