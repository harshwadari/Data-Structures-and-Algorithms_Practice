# Number of Distinct Islands
"""
Given a grid grid[][] of size n × m, consisting of characters 'L' and 'W', where 'L' represents Land and 'W' represents Water, find the number of distinct islands in the grid. An island is a group of one or more land cells connected horizontally or vertically.

Two islands are considered distinct if their shapes are different.
Two islands have the same shape if one can be translated to match the other exactly. Rotation and reflection are not allowed.
Examples :

Input: grid[][] = [['L', 'W', 'W'], ['W', 'W', 'L'], ['L', 'W', 'W']]
Output: 1
Explanation: The grid contains three islands. All these islands have the same shape (a 1 × 1 block of land), so they are counted as a single distinct island.

"""
# DFS Appraoch 

class Solution:
    def dfs(self,r,c,br,bc,rows,cols,grid,visited,shape):
        visited[r][c] = 1
        shape.append((r-br,c-bc))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for x,y in directions:
            newI = r + x
            newJ = c + y
            if newI < 0 or newJ < 0 or newI >= rows or newJ >= cols:
                continue
            if grid[newI][newJ] == 'W':
                continue
            if visited[newI][newJ] == 1:
                continue
            self.dfs(newI,newJ,br,bc,rows,cols,grid,visited,shape)
    def countDistinctIslands(self, grid):
        # code here
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        islands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and visited[i][j] == 0:
                    shape = []
                    self.dfs(i,j,i,j,rows,cols,grid,visited,shape)
                    islands.add(tuple(shape))
        return len(islands)