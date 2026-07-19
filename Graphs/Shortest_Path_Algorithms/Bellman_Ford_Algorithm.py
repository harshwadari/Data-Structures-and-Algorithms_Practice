# Bellman Ford Algorithm
"""
Given an weighted graph with V vertices numbered from 0 to V-1 and E edges, 
represented by a 2d array edges[][], where edges[i] = [u, v, w] represents a 
direct edge from node u to v having w edge weight. You are also given a source vertex src.

Your task is to compute the shortest distances from the source to all other 
vertices. If a vertex is unreachable from the source, its distance should be 
marked as 108. Additionally, if the graph contains a negative weight cycle, 
return [-1] to indicate that shortest paths cannot be reliably computed.

Examples:

Input: V = 5, edges[][] = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], src = 0

Output: [0, 5, 6, 6, 7]
Explanation: Shortest Paths:
For 0 to 1 minimum distance will be 5. By following path 0 → 1
For 0 to 2 minimum distance will be 6. By following path 0 → 1  → 2
For 0 to 3 minimum distance will be 6. By following path 0 → 1  → 2 → 4 → 3 
For 0 to 4 minimum distance will be 7. By following path 0 → 1  → 2 → 4

Constraints:
1 ≤ V ≤ 100
1 ≤ E = edges.size() ≤ V*(V-1)
-1000 ≤ w ≤ 1000
0 ≤ src < V
"""

# TC = O(V*E) and SC = O(V)
class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        distance = [10 ** 8 for _ in range(V)]
        distance[src] = 0
        for _ in range(V-1):
            for u,v ,w in edges:
                if distance[u] != 10 ** 8:
                    if distance[u] + w < distance[v]:
                        distance[v] = distance[u] + w
        for u,v ,w in edges:
                if distance[u] != 10 ** 8:
                    if distance[u] + w < distance[v]:
                        return [-1]
        return distance