n = int(input())
c = list(map(int,input().split()))

ver = (0, '')
rev = (0, '')

for i in range(n):
    s = input().rstrip('\r\n')
    r = s[::-1]

    y = 1e16
    n = 1e16
 
    print("Iteration... ver=%s rev=%s s=%s r=%s" % (ver, rev, s, r))

    if ver[1] <= s:
        print("(case 1) n = %s" % ver[0])
        n = ver[0]
    if rev[1] <= s:
        print("(case 2) n = %s" % min(n, rev[0]))
        n = min(n, rev[0])
    if ver[1] <= r:
        print("(case 3) y = %s" % (ver[0] + c[i]))
        y = ver[0] + c[i]
    if rev[1] <= r:
        print("(case 4) y = %s" % min(y, rev[0] + c[i]))
        y = min(y, rev[0] + c[i])
	
        ver = (n, s)
        rev = (y, r)
        print("(n=%s, s=%s)(y=%s, r=%s)" % (n, s, y, r))


sol = min(ver[0], rev[0])
print("sol = min(%s, %s)" % (ver[0], rev[0]))

if sol < 1e15 :
    print(sol)
else:
    print(-1)
