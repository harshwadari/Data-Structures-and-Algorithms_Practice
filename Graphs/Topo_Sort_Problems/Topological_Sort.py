# Topolocial Sort using dfs
"""
TC :
O(V+E)+O(V+E)+O(V)

= O(2V+2E+V)

= O(3V+2E)

Ignoring constants,

TC = O(V + E)

SC :

Adjacency List   O(V + E)

Visited          O(V)

Answer Stack     O(V)

Recursion Stack  O(V)
O(V+E)+O(V)+O(V)+O(V)

= O(4V+E)

Ignoring constants,

SC = O(V + E)
"""
class Solution:
    def dfs(self,node,visited,stack,adjlist):
        visited[node] = 1
        for adjnode in adjlist[node]:
            if visited[adjnode] == 0:
                self.dfs(adjnode,visited,stack,adjlist)
        stack.append(node)
    def topoSort(self, V, edges):
        # Code here
        adjlist = [[] for _ in range(V)]
        for u,v in edges:
            adjlist[u].append(v)
        visited = [0] * V
        stack = []
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i,visited,stack,adjlist)
        return stack[ : : -1 ]