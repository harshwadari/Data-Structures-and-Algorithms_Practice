# DFS Traversal of Graph 
# TC O(V + E) where v is vertex and E is edges and SC = O(V)
class Solution:
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited = [0] * (n + 1)
        result = []
        def dfshelper(node):
            visited[node] = 1
            result.append(node)
            for m in adj[node]:
                if not visited[m]:
                    dfshelper(m)
        dfshelper(0)
        return result
