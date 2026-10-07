# Count Edges in Graph
"""
Given an undirected graph containing V vertices from 0 to V-1, represented by a 
2D adjacency list adj[][], where each adj[i] represents the list of vertices
 connected to vertex i. Your task is to count the total number of edges present in the graph.

Examples :

Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3], [2]]

Output: 4
Explanation: The edges in the graph are: (0-1), (0-2), (2-3), (1-2). Hence, total 
number of edges = 4.
Input: adj[][] = [[1], [0, 2], [1, 3], [2]]

Output: 3
Explanation: The edges in the graph are: (0-1), (1-2), (2-3). Hence, total number of edges = 3.
Constraints:
1 ≤ V = adj.size() ≤ 104
0 ≤ adj[i][j] < V
"""


# TC = O(V + E) and SC = O(1)

class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        edges = 0
        for i in range(len(adj)):
            edges += len(adj[i])
        return edges // 2