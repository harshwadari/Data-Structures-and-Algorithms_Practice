# Grid Paths from Top to Bottom Corner
"""
Given an n x m matrix mat[][], find all possible paths from the top-left cell 
(0, 0) to the bottom-right cell (n-1, m-1).

From each cell, movement is restricted to two directions:

Right → (i, j+1)
Down → (i+1, j)
Return all possible paths, where each path is represented as a list of matrix
 elements encountered along the way.

Examples:

Input: mat[][] = [[1, 2, 3], [4, 5, 6]]
Output: [[1, 4, 5, 6], [1, 2, 5, 6], [1, 2, 3, 6]]
Explanation: There are 3 possible paths from cell (0,0) to (1,2).
Input: mat[][] = [[1, 2], [3, 4]]
Output: [[1, 2, 4], [1, 3, 4]]
Explanation: There are 2 possible paths from cell (0,0) to (1,1).
Constraints:
1 <= n, m <= 10 
1 <= mat[i][j] <= n*m
n * m < 20
"""

# Time Complexity: O(2^(n + m) Auxiliary Space: O(n + m)
class Solution:
    def allPaths(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        path = []
        result = []
        def backtrack(row,col):
            if row == n -1 and col == m -1:
                path.append(mat[row][col])
                result.append(path[:])
                path.pop()
                return
            path.append(mat[row][col])
            if row + 1 < n:
                backtrack(row+1,col)
            if col + 1 < m:
                backtrack(row,col+1)
            path.pop()
        backtrack(0,0)
        return result
            