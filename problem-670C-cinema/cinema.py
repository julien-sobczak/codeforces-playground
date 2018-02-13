n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))

from collections import Counter
count = Counter(a)

max = 0
ans = -1

prev_count = 0

for i, (ai, counti) in enumerate(count.most_common()):
  if ai not in b: 
    # There is no film with the audio in this language
    continue
  
  #print(i, ai, counti, b, prev_count)
  if prev_count > counti:
    # Consider only films having the maximum of scientists speaking the audio language
    break
  
  # Inspect subtitles
  for j, bj in enumerate(b):
    if bj == ai:
      if c[j] > max:
        max = c[j]
        ans = j
  prev_count = counti

if ans == -1:
  for i, (ai, counti) in enumerate(count.most_common()):
    for j, cj in enumerate(c):
      print(j + 1)
      exit(0)

print(ans + 1)
