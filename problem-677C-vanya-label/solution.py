d=[0]*64
for i in range(64):
    for j in range(64):
        d[i&j]+=1
s=input()
ans=1
for i in s:
    if '0'<=i<='9':
        ans*=d[int(i)]
    elif 'A'<=i<='Z':
        ans*=d[ord(i)-ord('A')+10]
    elif 'a'<=i<='z':
        ans*=d[ord(i)-ord('a')+10+26]
    elif i=='-':
        ans*=d[62]
    elif i=='_':
        ans*=d[63]
    ans%=10**9+7
    
print(ans)
