# Cycle detection in directed graph using dfs
"""
------------------------------------------------------------
Time Complexity
------------------------------------------------------------

| Operation                                 | Complexity |
|-------------------------------------------|------------|
| Create adjacency list                     | O(V)       |
| Insert all edges into adjacency list      | O(E)       |
| Initialize visited array                  | O(V)       |
| Initialize path_visited array             | O(V)       |
| DFS traversal (visit every vertex once)   | O(V)       |
| Traverse all adjacency lists (all edges)  | O(E)       |
| Overall Time Complexity                   | O(V + E)   |


------------------------------------------------------------
Space Complexity
------------------------------------------------------------

| Data Structure            | Complexity |
|---------------------------|------------|
| Adjacency List            | O(V + E)   |
| visited array             | O(V)       |
| path_visited array        | O(V)       |
| DFS Recursion Stack       | O(V)       |
| Overall Space Complexity  | O(V + E)   |

"""
class Solution:
    def dfs(self,node,visited,path_visited,adjlist):
        visited[node] = 1
        path_visited[node] = 1
        for adjnode in adjlist[node]:
            if visited[adjnode] == 0:
                x = self.dfs(adjnode,visited,path_visited,adjlist)
                if x == True:
                    return True
            elif path_visited[adjnode] == 1:
                return True
        path_visited[node] = 0
        return False
    def isCyclic(self, V, edges):
        # code here
        adjlist = [[] for _ in range(V)]
        for u , v in edges:
            adjlist[u].append(v)
        visited = [0] * V
        path_visited  = [0] * V
        for i in range(V):
            if visited[i] == 0:
                ans = self.dfs(i,visited,path_visited,adjlist)
                if ans == True:
                    return True
        return False
    
"""

------------------------------------------------------------
Time Complexity
------------------------------------------------------------

| Operation                                    | Complexity |
|----------------------------------------------|------------|
| Create adjacency list                        | O(V)       |
| Initialize indegree array                    | O(V)       |
| Insert all edges into adjacency list         | O(E)       |
| Compute indegree of each vertex              | O(E)       |
| Push all 0-indegree vertices into queue      | O(V)       |
| Kahn's BFS (visit every vertex once)         | O(V)       |
| Traverse all adjacency lists (all edges)     | O(E)       |
| Overall Time Complexity                      | O(V + E)   |


------------------------------------------------------------
Space Complexity
------------------------------------------------------------

| Data Structure            | Complexity |
|---------------------------|------------|
| Adjacency List            | O(V + E)   |
| Indegree Array            | O(V)       |
| Queue                     | O(V)       |
| Result Array              | O(V)       |
| Overall Space Complexity  | O(V + E)   |

"""
 
# BFS Approach
from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Code here
        adjlist = [[] for _ in range(V)]
        indegree = [0] * V
        for u,v in edges:
            adjlist[u].append(v)
            indegree[v] += 1
        queue = deque()
        result = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node)
            for adjnode in adjlist[node]:
                indegree[adjnode] -= 1
                if indegree[adjnode] == 0:
                    queue.append(adjnode)
        if len(result) == V:
            return False
        return True