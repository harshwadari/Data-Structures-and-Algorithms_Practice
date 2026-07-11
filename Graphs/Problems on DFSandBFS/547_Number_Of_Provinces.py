# 547. Number of Provinces
"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected 
directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and 
no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 
1 if the ith city and the jth city are directly connected, and 
isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


# DFS Appraoch as a separate function GFG 
def dfs(self,node,visited,adjlist):
    visited[node] = 1
    for adjnode in adjlist[node]:
        if visited[adjnode] == 0:
            self.dfs(adjnode,visited,adjlist)
        
def countConnected(self, V, edges):
    # code here 
    adjlist = [[] for _ in range(V)]
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
    visited = [0] * V
    count = 0
    for i in range(0,V):
        if visited[i] == 0:
            count += 1
            self.dfs(i,visited,adjlist)
    return count

# LC dfs appraoch
class Solution(object):
    def dfs(self,node,visited,isConnected):
        visited[node] = 1
        for adjnode in range(len(isConnected)):
            if isConnected[node][adjnode] == 1 and visited[adjnode] == 0:
                self.dfs(adjnode,visited,isConnected)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count += 1
                self.dfs(i,visited,isConnected)
        return count
                                        

# BFS Approach 
from collections import deque

class Solution:

    def bfs(self, start, isConnected, visited):
        q = deque()
        q.append(start)
        visited[start] = 1

        while q:
            node = q.popleft()

            for nei in range(len(isConnected)):
                if isConnected[node][nei] == 1 and visited[nei] == 0:
                    visited[nei] = 1
                    q.append(nei)

    def findCircleNum(self, isConnected):
        V = len(isConnected)

        visited = [0] * V
        provinces = 0

        for i in range(V):
            if visited[i] == 0:
                provinces += 1
                self.bfs(i, isConnected, visited)

        return provinces