# 200. Number of Islands
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
# dfs appraoch 
class Solution:
    def dfs(self,i,j,grid,rows,cols):
        if i < 0 or j < 0 or i >= rows or  j >= cols:
            return
        if grid[i][j] == 'W':
            return
        grid[i][j] = 'W'
        self.dfs(i - 1, j, grid, rows, cols)
        self.dfs(i + 1, j, grid, rows, cols)
        self.dfs(i, j - 1, grid, rows, cols)
        self.dfs(i, j + 1, grid, rows, cols)
        self.dfs(i - 1, j - 1, grid, rows, cols)
        self.dfs(i - 1, j + 1, grid, rows, cols)
        self.dfs(i + 1, j - 1, grid, rows, cols)
        self.dfs(i + 1, j + 1, grid, rows, cols)
    def numIslands(self, grid):
        # code here
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j  in range(cols):
                if grid[i][j] =='L':
                    count += 1
                    self.dfs(i,j,grid,rows,cols)
        return count