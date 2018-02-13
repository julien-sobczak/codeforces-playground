from math import factorial

def binomial(n, m):
    if m < 0 or m > n:
        return 0
    m = min(m, n - m)
    return factorial(n) // factorial(m) // factorial(n-m)
    
def main():
    n, m, t = map(int, input().split())
    # Work in reverse. Substract impossible combinaisons!
    print(binomial(n + m, t) - binomial(m, t) - binomial(m, t - 1) * n - 
         binomial(m, t - 2) * binomial(n, 2) - binomial(m, t - 3) * binomial(n, 3) - 
         binomial(n, t))

main()
