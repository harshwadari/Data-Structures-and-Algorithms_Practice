# 73. Set Matrix Zeroes

"""
Idea:

When a 0 is found, mark all non-zero elements in its row and column as a temporary value (inf).
Don't directly change them to 0, otherwise newly created zeros will affect other rows/columns incorrectly.
After processing all original zeros, convert all inf values to 0.

Steps:

Traverse matrix.
For every 0, mark its row and column with inf (except existing zeros).
Traverse again and replace all inf with 0.

Why use inf?

To distinguish between:
Original zeros
Cells that should become zero later

Time Complexity:

For each zero, traverse its entire row and column.
Worst case: O((m × n) × (m + n))

Space Complexity:

O(1) (ignoring the marker value)
"""


class Solution(object):
    def markInfinity(self,matrix,row,col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,r):
            if matrix[i][col] != 0:
                matrix[i][col] = float('inf')
        for j in range(0,c):
            if matrix[row][j] != 0:
                matrix[row][j] = float('inf')
        

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] ==  0:
                    self.markInfinity(matrix,i,j)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
            
# optimal approach 
# TC = O(2(N*M)) SC = O(N+M)

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowTrack = [0] * rows
        colTrack = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowTrack[i] = -1
                    colTrack[j] = -1
        for i in range(rows):
            for j in range(cols):
                if rowTrack[i] == -1 or colTrack[j] == -1:
                    matrix[i][j] = 0