# 2685. Count the Number of Complete Components
"""
You are given an integer n. There is an undirected graph with n vertices, 
numbered from 0 to n - 1. You are given a 2D integer array edges where 
edges[i] = [ai, bi] denotes that there exists an undirected edge connecting 
vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a 
path between any two vertices, and no vertex of the subgraph shares an 
edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between 
every pair of its vertices.
"""

# BFS approach
"""
TC :
Create adjacency list      O(n)

Insert edges               O(m)

Outer loop                 O(n)

BFS nodes                  O(n)

Traverse neighbors         O(m)

O(n) + O(m) + O(n) + O(n) + O(m)

= O(3n + 2m)

= O(n + m)
SC :
Total Space
Adjacency list     O(n + m)

Visited            O(n)

Queue              O(n)
= O(n + m + n + n)

= O(3n + m)

= O(n + m)
"""
from collections import deque
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adjlist = [[] for _ in range(n)]
        for u , v in edges:
            adjlist[v].append(u)
            adjlist[u].append(v)
        visited = [0] * n
        count = 0
        for i in range(0,n):
            if visited[i] == 1:
                continue
            queue = deque()
            queue.append(i)
            visited[i] = 1
            vertices = 0
            degree = 0
            while len(queue) != 0:
                node = queue.popleft()
                vertices += 1
                degree += len(adjlist[node])
                for adjnode in adjlist[node]:
                    if visited[adjnode] == 0:
                        visited[adjnode] = 1
                        queue.append(adjnode)
            actualedges = degree // 2
            required = vertices * (vertices - 1) // 2
            if actualedges == required:
                count += 1
        return count
