# Connected Components in a Graph
"""
Given a undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges. 
The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi. We say 
two vertices u and v belong to a same component if there is a path from u to v or v to u. 
Find the number of connected components in the graph.



A connected component is a subgraph of a graph in which there exists a path between 
any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.


Example 1



Input: V=4, edges=[[0,1],[1,2]]

Output: 2

Explanation: Vertices {0,1,2} forms the first component and vertex 3 forms the second component.
"""

# Optimal Appraoch using BFS Approach
"""
Overall TC = O(3V + 2E) ~O(V + E) and SC = O()
"""
from collections import deque
def components(V:int,edges:list[list[int]]) ->int:
    adjlist = [[] for _ in range(V)] # empty list creation TC = O(V)
    for u,v in edges: # TC = O(E)
        adjlist[u].append(v)
        adjlist[v].append(u)
    visited = [0] * V # TC = O(V)
    count = 0
    for i in range(V): # TC = O(V)
        if visited[i] == 0:
            count += 1
            queue = deque()
            queue.append(i)
            visited[i] = 1
            while len(queue) != 0: # TC = O(V)
                node = queue.popleft()
                for adjnode in adjlist[node]: # TC = O(E)
                    if visited[adjnode] == 0:
                        visited[adjnode] = 1
                        queue.append(adjnode)
    return count 






# DFS Approach
def dfs(node, adjlist, visited):
    visited[node] = 1                  # O(1)

    for adjnode in adjlist[node]:      # Overall O(E)
        if visited[adjnode] == 0:
            dfs(adjnode, adjlist, visited)


def componentsdfs(V, edges):

    adjlist = [[] for _ in range(V)]   # O(V)

    for u, v in edges:                 # O(E)
        adjlist[u].append(v)           # O(1)
        adjlist[v].append(u)           # O(1)

    visited = [0] * V                  # O(V)

    count = 0                          # O(1)

    for i in range(V):                 # O(V)

        if visited[i] == 0:
            count += 1                 # O(1)
            dfs(i, adjlist, visited)   # Overall O(V + E)

    return count



# BFS approach for gfg connected problem where instead of counting components to be store

from collections import deque
class Solution:
    def getComponents(self, V, edges):
        # code here
        adjlist = [[] for _ in range(V)]
        for u , v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visited = [0] * V
        result = []
        for i in range(V):
            if visited[i] == 0:
                component = []
                queue = deque()
                queue.append(i)
                visited[i] = 1
                while len(queue) != 0:
                    node = queue.popleft()
                    component.append(node)
                    for adjnode in adjlist[node]:
                        if visited[adjnode] == 0:
                            visited[adjnode] = 1
                            queue.append(adjnode)
                result.append(component)
        return result






# DFS approach for gfg connected problem where instead of counting components to be store
def dfs(node,adjlist,visited,component):
    visited[node] = 1
    component.append(node)
    for adjnode in adjlist[node]:
        if visited[adjnode] == 0:
            dfs(adjnode,adjlist,visited,component)
def gfgcompo(V,edges):
    adjlist = [[] for _ in range(V)]
    for u,v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
    visited = [0] * V
    result = []
    for i in range(V):
        if visited[i] == 0:
            component = []
            dfs(i,adjlist,visited,component)
            result.append(component)
    return result