# Convert Adjacency matrix to Adjacency list
"""
You are given an undirected graph represented by its adjacency matrix mat[][],
 where mat[i][j] = 1 indicates that there is an edge between vertex i and vertex j, 
 and mat[i][j] = 0 indicates no edge.
Your task is to convert the given adjacency matrix into its corresponding adjacency
 list representation.
In the resulting adjacency list, each element adj[i] should contain all vertices
 that are directly connected to vertex i.

Examples :

Input: mat[][] = [[0, 1, 0, 1], 
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]
Output: [[1, 3], [0, 2], [1, 3], [0, 2]]
Explanation: 
    
The adjacency matrix represents the graph above and hence the adjacency list is 
[[1, 3], [0, 2], [1, 3], [0, 2]].
Input: mat[][] = [[0, 1, 1, 0, 0], 
               [1, 0, 1, 0, 0], 
               [1, 1, 0, 1, 1], 
               [0, 0, 1, 0, 0], 
               [0, 0, 1, 0, 0]]
Output: [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
Explanation: 
   
The adjacency matrix represents the graph above and hence the adjacency list is 
[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]].
Constraints:
1 ≤ V = mat.size() ≤ 100
1 ≤ mat[0].size() ≤ 100
"""

# TC = O(N ^ 2) and SC = O(N^2)
class Solution:
    def matToAdj(self, mat):
        # code here
        n = len(mat)
        result = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1:
                    result[i].append(j)
        return result