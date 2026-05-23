# 48. Rotate Image

"""
You are given an n x n 2D matrix representing an image, rotate the 
image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify 
the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

"""
Brute force inuition   index manipulation

Core Brute Force Intuition

Think about where each element moves after rotation.

If an element is at position:

(i, j)

After 90° clockwise rotation, it goes to:

(j, n - 1 - i)

So the idea of brute force is simple:

Create a new matrix

For every element in the original matrix

Put it in its rotated position in the new matrix

Why this formula works

Take this matrix:

1 2 3
4 5 6
7 8 9

Coordinates:

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

Let's move some elements.

Example 1

Element 1

(0,0)

New position:

(j, n-1-i)
(0, 3-1-0)
(0,2)

So 1 → (0,2)

Example 2

Element 2

(0,1)

New position:

(1, 2)
Example 3

Element 7

(2,0)

New position:

(0,0)

That is exactly what happens in rotation.

Brute Force Logic

Create new_matrix of size n × n

Traverse original matrix

Move element to rotated position

"""

# TC = O(N^2) and SC = O(N^2)
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][(n-1)-i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]



# optimal one 
"""
using transpose and reverse 
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

     

