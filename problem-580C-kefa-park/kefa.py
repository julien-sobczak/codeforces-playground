n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

class Graph:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.e = {}
   
    def edge(self, x, y):
        if x not in self.e:
            self.e[x] = [y]
        else
            self.e[x].append(y)

    def solve(self):
        for e in self.e[1]

g = Graph(n, m)
for _ in range(n - 1):
    x, y = list(map(int, input().split()))
    g.edge(x, y)

print(g.solve())
