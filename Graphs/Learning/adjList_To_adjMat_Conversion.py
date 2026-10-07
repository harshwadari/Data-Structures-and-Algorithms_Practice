# Convert Adjacency List to Adjacency Matrix
"""
You are given an directed graph in the form of an adjacency list, where each element 
adj[i] contains a list of all vertices adjacent to vertex i.
Your task is to convert this adjacency list into an adjacency matrix representation.

Examples :

Input: adj[][] = [[1, 3], [2], [], [2]]
   1
Output: 
[[0, 1, 0, 1],
[0, 0, 1, 0],
[0, 0, 0, 0],
[0, 0, 1, 0]]
Explanation: The edges in the graph are (0, 1), (0, 3), (1, 2), and (3, 2). Hence, 
in the adjacency matrix, the cells (0,1), (0,3), (1,2) and (3,2) are marked as 1.
Input: adj[][] = [[1, 2], [2], [3, 4], [0], []]

Output: 
[[0, 1, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0], 
[0, 0, 0, 0, 0]] 
Explanation: The edges in the graph are (0, 1), (0, 2), (1, 2), (2, 3), (2, 4) and 
(3, 0). Hence, in the adjacency matrix, the cells (0,1), (0,2), (1,2), (2,3), (2,4) and
 (3,0) are marked as 1.
Constraints:
1 ≤ V = adj.size() ≤ 104
0 ≤ adj[i][j] < V
"""
# TC = O(N ^ 2) and SC = O(N ^ 2)
class Solution: 
    def adjToMat(self, adj):
        # code here
        n = len(adj)
        result = [[0 for _ in range(n)] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                result[u][v] = 1
        return result
            