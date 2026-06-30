# 37. Sudoku Solver
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

# Optimal approach using backtrack recursion 
# TC = O(9 ^N) and SC = O(N) where N is recursion depth stack space 
class Solution:
    def isValid(self,board,row,col,num):
        for r in range(9):
            if board[row][r] == num:
                return False
        for c in range(9):
            if board[c][col] == num:
                return False
        startrow = (row//3) * 3
        startcol = (col//3) * 3
        for r in range(startrow,startrow+3):
            for c in range(startcol,startcol+3):
                if board[r][c] == num:
                    return False
        return True
    def backtrack(self,board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1,10):
                        if self.isValid(board,r,c,num):
                            board[r][c] = num
                            if self.backtrack(board):
                                return True
                            else:
                                board[r][c] = 0
                    return False
        return True
    def solveSudoku(self, board):
        # code here
        self.backtrack(board)