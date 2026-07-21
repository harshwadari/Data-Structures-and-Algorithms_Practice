# 980. Unique Paths III
"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending 
square, that walk over every non-obstacle square exactly once.

 Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.

"""

# Recursive Approach using dfs and backtracking
# TC = O(4 ^ i *j) and SC = O(i + j)
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        startrow = 0
        startcol = 0
        remain = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    remain += 1
                if grid[i][j] == 1:
                    startrow = i
                    startcol = j
        def backtrack(i,j,remain):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 0
            if grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                if remain == 1:
                    return 1
                return 0
            temp = grid[i][j]
            grid[i][j] = -1
            remain -= 1
            up = backtrack(i-1,j,remain)
            down = backtrack(i+1,j,remain)
            left = backtrack(i,j-1,remain)
            right = backtrack(i,j+1,remain)
            grid[i][j] = temp
            return left + up + down + right
        return backtrack(startrow,startcol,remain)