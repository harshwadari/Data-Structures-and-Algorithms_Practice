# BFS Traversal of a graph

"""

------------------------------------------------------------
Time Complexity
------------------------------------------------------------

| Operation                                    | Complexity |
|----------------------------------------------|------------|
| Initialize visited array                     | O(V)       |
| Create queue                                 | O(1)       |
| Push source vertex into queue                | O(1)       |
| Visit each vertex exactly once               | O(V)       |
| Pop each vertex from queue                   | O(V)       |
| Traverse all adjacency lists (all edges)     | O(E)       |
| Check visited[] for each adjacent vertex     | O(E)       |
| Push unvisited vertices into queue           | O(V)       |
| Append vertices to result list               | O(V)       |
| Overall Time Complexity                      | O(V + E)   |


------------------------------------------------------------
Space Complexity
------------------------------------------------------------

| Data Structure            | Complexity |
|---------------------------|------------|
| Adjacency List (Input)    | O(V + E)   |
| Visited Array             | O(V)       |
| Queue                     | O(V)       |
| Result List               | O(V)       |
| Auxiliary Space           | O(V)       |
| Overall Space (Including Input) | O(V + E) |

"""
from collections import deque
def bfs(adj:list[list[int]]) -> list[int]:
    visited = [0] * len(adj)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    result = []
    while len(queue) != 0:
        node = queue.popleft()
        result.append(node)
        for adjnode in adj[node]:
            if visited[adjnode] == 0:
                queue.append(adjnode)
                visited[adjnode] = 1
    return result
print(bfs([[], [2, 8], [1, 3, 4], [2], [2, 5], [4, 6], [5, 7], [6, 8], [1, 7, 9], [8]]))  