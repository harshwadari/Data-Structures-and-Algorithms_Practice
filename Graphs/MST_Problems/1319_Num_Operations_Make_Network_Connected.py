# 1319. Number of Operations to Make Network Connected
"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections 
forming a network where connections[i] = [ai, bi] represents a connection between computers 
ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between 
two directly connected computers, and place them between any pair of disconnected computers to 
make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers 
connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.

"""


# Naive Approach using just count number of connected conmponents and return count - 1
from collections import deque
def makeConnected(V:int,edges:list[list[int]]) -> int:
    if len(edges) < V - 1:
        return - 1
    adjlist = [[] for _ in range(V)]
    visited = [0] * V
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
    count = 0
    for i in range(V):
        if visited[i] == 0:
            count += 1
        queue = deque()
        queue.append(i)
        visited[i] = 1
        while len(queue) != 0:
            node = queue.popleft()
            for adjnode in adjlist[node]:
                if visited[adjnode] == 0:
                    visited[adjnode] = 1
                    queue.append(adjnode)
    return count  - 1



# DFS Approach 
def dfsConnected(V,edges):
    if len(edges) < V - 1:
        return -1
    adjlist = [[] for _ in range(V)]
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(v)
    visited = [0] * V
    count = 0
    def dfs(node):
        visited[node] = 1
        for adjnode in adjlist[node]:
            if visited[adjnode] == 0:
                dfs(adjnode)
    for i in range(V):
        if visited[i] == 0:
            count += 1
            dfs(i)
    return count - 1