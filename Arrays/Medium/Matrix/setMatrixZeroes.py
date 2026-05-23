# Set Matrix Zeroes
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


# brure approach

"""
brute intuition 
mark all rows and cols of zero element with infinity 
and then make infinity to zero
"""

# TC = O((mn)(m+n)) and SC = O(1)
class Solution(object):
    def mark(self,matrix,rows,cols):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,r):
            if matrix[i][cols] != 0:
                matrix[i][cols] = float('inf')
        for j in range(0,c):
            if matrix[rows][j] != 0:
                matrix[rows][j] = float('inf')
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix) 
        c = len(matrix[0])
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    self.mark(matrix,i,j)
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
        

#optimal appraoch
"""
by maintaining a row and column tracker

"""
# TC = O(N*M) and SC = O(N + M )

def matrixzeroess(matrix):
    r = len(matrix)
    c = len(matrix[0])
    rowtracker = [0 for _ in range(r)]
    coltracker = [ 0 for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowtracker[i] = -1
                coltracker[j] = -1
    for i in range(r):
        for j in range(c):
            if rowtracker[i] == -1 or coltracker[j] == -1:
                matrix[i][j] == 0
