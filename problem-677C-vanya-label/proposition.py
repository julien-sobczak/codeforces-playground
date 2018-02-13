s = input()

n = 0
for l in s:
  if '0' <= l <= '9':
    n += 0 + ord(l) - ord('0')
  elif 'A' <= l <= 'Z':
    n += 10 + ord(l) - ord('A')
  elif 'a' <= l <= 'z':
    n += 36 + ord(l) - ord('a')
  elif l == '-':
    n += 62
  elif l == '_':
    n += 63

zeros = format(n, "b").count('0')

ans = 2 ** zeros
print(ans)

