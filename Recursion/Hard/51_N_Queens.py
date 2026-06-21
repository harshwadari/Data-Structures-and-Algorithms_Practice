# 51. N-Queens
"""
The n-queens puzzle is the problem of placing n 
queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to 
the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration 
of the n-queens' placement, where 'Q' and '.' both indicate a 
queen and an empty space, respectively.
 
"""

class Solution(object):
    def backtrack(self,col,board,ans,leftrow,upperdiagonal,lowerdiagonal,n):
        if col == n:
            ans.append(board[:])
            return
        for row in range(n):
            if(
                leftrow[row] == 0 and lowerdiagonal[row + col] == 0
                and upperdiagonal[n - 1 + col - row] == 0
                ):
                board[row] = board[row][:col] + 'Q' + board[row][col + 1 :]
                leftrow[row] = 1
                lowerdiagonal[row + col] = 1
                upperdiagonal[n - 1 + col - row] = 1
                self.backtrack(col + 1,board,ans , leftrow,upperdiagonal,lowerdiagonal,n)
                board[row] = board[row][:col] + '.' + board[row][col + 1 :]
                leftrow[row] = 0
                lowerdiagonal[row + col] = 0
                upperdiagonal[n - 1 + col - row] = 0
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = ['.' * n for _ in range(n)]
        leftrow = [0] * n
        upperdiagonal = [0] * (2 * n - 1)
        lowerdiagonal = [0] * (2 * n - 1)
        self.backtrack(0,board,ans,leftrow,upperdiagonal,lowerdiagonal,n)
        return ans
