n, k = map(int, input().split())
s = input()
res = 0
a = 0
b = 0
l = 0
for r in range(n):
	if s[r] == 'a': a +=1
	else: b += 1
	
	if min(a,b) > k:
		if s[l] == 'a': a -= 1
		else: b -= 1
		l += 1
	else: res +=1
print(res)
