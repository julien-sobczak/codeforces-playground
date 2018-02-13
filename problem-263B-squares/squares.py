n, k = map(int, input().split())
a = [int(a) for a in input().split()]

# We just have to find a point on the extremity of the n-kth square
a.sort(reverse=True)
if k > n:
    print('-1')
else:
    print(a[k-1], a[k-1])
