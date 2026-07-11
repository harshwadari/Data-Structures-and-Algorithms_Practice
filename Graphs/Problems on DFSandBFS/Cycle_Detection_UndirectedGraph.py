# Cycle Detection in undirected graph

# BFS Appraoch 

from collections import deque
def isCycle(self, V, edges):
    adjlist = [[] for _ in range(V)]
    for u , v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
    visited = [0] * V
    for i in range(0,V):
        if visited[i] == 1:
            continue
        queue = deque()
        queue.append((i,-1))
        visited[i] = 1
        while len(queue) != 0:
            node, parent = queue.popleft()
            for adjnode in adjlist[node]:
                if visited[adjnode] == 0:
                    visited[adjnode] = 1
                    queue.append((adjnode,node))
                else:
                    if adjnode != parent:
                        return True
    return False

# DFS Approach 
class Solution:
    def dfs(self,node,parent,visited,adjlist):
        visited[node] = 1
        for adjnode in adjlist[node]:
            if visited[adjnode] == 0:
                ans = self.dfs(adjnode,node,visited,adjlist)
                if ans == True:
                    return True
            elif visited[adjnode] == 1 and adjnode != parent:
                return True
        return False
    
    def graph(self,V,edges):
        adjlist = [[] for _ in range(V)]
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visited = [0] * V
        for i in range(V):
            if visited[i] == 0:
                continue
            if self.dfs(i,-1,visited,adjlist) == True:
                return True
        return False