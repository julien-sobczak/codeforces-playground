n = int(input())
m = 10 ** 9

mi = 1


while True:  # We try on small numbers first
    for i in range(1, mi):  # If we set m directly, the program takes a long time even for basic cases
        for j in range(1, mi):
            for k in range(1, mi):
                if i == j or j == k or i == k: 
                    continue
                q = 1 * j * k + i * 1 *  k + i * j * 1
                d = i * j * k
 
                if (q * n / d) == 2:
                    print(i, j, k)
                    exit(0)
    mi += 1
    if mi > m:
        print(-1) 
        exit(0)

