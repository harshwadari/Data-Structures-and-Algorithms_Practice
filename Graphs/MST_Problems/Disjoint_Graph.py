class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1


ds = Disjoint(7)

ds.union(1, 2)
ds.union(2, 3)
ds.union(3, 4)
ds.union(4, 5)
ds.union(6, 2)
ds.union(5, 6)
ds.union(3, 7)

print(ds.find(1))
print(ds.find(7))