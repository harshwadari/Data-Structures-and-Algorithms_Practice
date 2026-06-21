# 52. N-Queens II
"""
The n-queens puzzle is the problem of placing n 
queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

class Solution(object):
    def backtrack(self,col,leftrow,upperdiagonal,lowerdiagonal,n):
        if col == n:
            self.count += 1
            return
        for row in range(n):
            if(
                leftrow[row] == 0 and lowerdiagonal[row + col] == 0
                and upperdiagonal[n - 1 + col - row] == 0
                ):
                leftrow[row] = 1
                lowerdiagonal[row + col] = 1
                upperdiagonal[n - 1 + col - row] = 1
                self.backtrack(col + 1,leftrow,upperdiagonal,lowerdiagonal,n)
                leftrow[row] = 0
                lowerdiagonal[row + col] = 0
                upperdiagonal[n - 1 + col - row] = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        leftrow = [0] * n
        upperdiagonal = [0] * (2 * n - 1)
        lowerdiagonal = [0] * (2 * n - 1)
        self.backtrack(0,leftrow,upperdiagonal,lowerdiagonal,n)
        return self.count