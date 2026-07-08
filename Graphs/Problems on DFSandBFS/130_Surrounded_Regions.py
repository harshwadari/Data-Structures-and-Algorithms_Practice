# 130. Surrounded Regions
"""
You are given an m x n matrix board containing letters 'X' and 'O', capture 
regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on
 the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the 
original board. You do not need to return anything.
"""

# Better  approach  using dfs and matrix traversion 
# TC = O(Rows * cols) + O(rows * cols) + O(r*c*4) dfs  and TC = O(R*C) + O(R*C) stack space
def dfs(self,i,j,board,visited,rows,cols):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return
    if visited[i][j] == 1:
        return
    if board[i][j] == 'X':
        return
    visited[i][j] = 1
    self.dfs(i - 1,j,board,visited,rows,cols)
    self.dfs(i,j - 1,board,visited,rows,cols)
    self.dfs(i ,j+1,board,visited,rows,cols)
    self.dfs(i +1,j,board,visited,rows,cols)
def solve(self, board):
   
    rows = len(board)
    cols = len(board[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                if board[i][j] == 'O':
                    if visited[i][j] == 0:
                        self.dfs(i,j,board,visited,rows,cols)
    for i  in range(rows):
        for j in range(cols):
            if board[i][j] == 'O' and visited[i][j] == 0:
                board[i][j] ='X'