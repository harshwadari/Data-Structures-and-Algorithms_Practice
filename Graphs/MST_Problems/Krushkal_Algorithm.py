# Krushkal Algorithm to find mst in graph in most optimal way 
"""
Kruskal's Algorithm is a greedy approach that helps us construct the MST by 
sorting all edges by weight and connecting components without forming cycles.
"""
class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True


class Solution:
    def spanningTree(self, V, edges):
        # edges = [[u, v, wt], ...]

        edges.sort(key=lambda x: x[2])   # Sort by weight

        ds = Disjoint(V)
        mst_weight = 0

        for u, v, wt in edges:
            if ds.union(u, v):
                mst_weight += wt

        return mst_weight