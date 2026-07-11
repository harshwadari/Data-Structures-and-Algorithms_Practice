# Topological Sort using BFS also known as Khans Algorithm 
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
        return result