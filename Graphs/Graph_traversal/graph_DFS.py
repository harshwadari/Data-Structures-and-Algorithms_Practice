# DFS Traversal of Graph 
# TC O(V + E) where v is vertex and E is edges and SC = O(V)
class Solution:
    def dfs(self, adj):
        visited = [0] * len(adj)
        result = []
        def dfshelper(node):
            visited[node] = 1
            result.append(node)
            for m in adj[node]:
                if not visited[m]:
                    dfshelper(m)
        dfshelper(0)
        return result


# different format approach 

class Solution:
    def helper(self,node,result,visited,adjlist):
        visited[node] = 1
        result.append(node)
        for adjnode in adjlist[node]:
            if visited[adjnode] == 0:
                self.helper(adjnode,result,visited,adjlist)
    def dfs(self, adj):
        # code here
        visited = [0] * len(adj)
        result = []
        self.helper(0,result,visited,adj)
        return result
    

# Coding ninjas approach 

from typing import *

def depthFirstSearch(V: int, E: int, edges: List[List[int]]):
    adj = [[] for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [0] * V
    ans = []

    def dfs(node, component):
        visited[node] = 1
        component.append(node)

        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei, component)

    for i in range(V):
        if not visited[i]:
            component = []
            dfs(i, component)
            component.sort()          # <-- important
            ans.append(component)

    return ans