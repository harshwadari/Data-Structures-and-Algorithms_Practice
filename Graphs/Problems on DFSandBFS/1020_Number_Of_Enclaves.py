# 1020. Number of Enclaves
"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land 
cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or
 walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of 
the grid in any number of moves.
"""

# Dfs appraoch 
"""
TC = O(r*c) + O(r*c) + O(r*c)
   = O(3*r*c)
   = O(r*c)
SC = O(r*c) recursive stack space
"""
def dfs(self,i,j,grid,rows,cols):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return
    if grid[i][j] == 0:
        return
    grid[i][j] = 0
    self.dfs(i - 1, j, grid, rows, cols)
    self.dfs(i + 1, j, grid, rows, cols)
    self.dfs(i, j - 1, grid, rows, cols)
    self.dfs(i, j + 1, grid, rows, cols)
def numEnclaves(self, grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j  in range(cols):
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                if grid[i][j] == 1:
                    self.dfs(i,j,grid,rows,cols)
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
    return count