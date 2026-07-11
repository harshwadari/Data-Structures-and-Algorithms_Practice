# 802. Find Eventual Safe States
"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
he graph is represented by a 0-indexed 2D integer array graph where graph[i] 
is an integer array of nodes adjacent to node i, meaning there is an edge 
from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe
 node if every possible path starting from that node leads to a terminal 
 node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer 
should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
"""

# bfs approach using reverse graph and toposort khans algorithm
"""
------------------------------------------------------------
Time Complexity
------------------------------------------------------------

| Operation                                    | Complexity |
|----------------------------------------------|------------|
| Create reverse graph                         | O(V)       |
| Reverse all edges & compute indegree         | O(E)       |
| Initialize queue                             | O(V)       |
| Kahn's BFS                                   | O(V)       |
| Traverse all reversed edges                  | O(E)       |
| Sort safe nodes                             | O(V log V) |
| Overall Time Complexity                      | O(V + E + V log V) |

------------------------------------------------------------
Space Complexity
------------------------------------------------------------

| Data Structure            | Complexity |
|---------------------------|------------|
| Reverse Graph             | O(V + E)   |
| Indegree Array            | O(V)       |
| Queue                     | O(V)       |
| Safe Nodes List           | O(V)       |
| Overall Space Complexity  | O(V + E)   |


"""
from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        V = len(graph)
        adjlist = [[] for _ in range(V)]
        indegree = [0] * V
        for node in range(V):
            for v in graph[node]:
                adjlist[v].append(node)
                indegree[node] += 1
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        result = []
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node)
            for adjnode in adjlist[node]:
                indegree[adjnode] -= 1
                if indegree[adjnode] == 0:
                    queue.append(adjnode)
        return sorted(result)
    

# gfg approach 
from collections import deque

class Solution:
    def safeNodes(self, V, edges):

        reverse = [[] for _ in range(V)]
        indegree = [0] * V

        for u, v in edges:
            reverse[v].append(u)
            indegree[u] += 1

        queue = deque()

        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for parent in reverse[node]:
                indegree[parent] -= 1
                if indegree[parent] == 0:
                    queue.append(parent)

        return sorted(result)