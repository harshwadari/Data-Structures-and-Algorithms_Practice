# Matrix Median

"""
Given a 2D array matrix that is row-wise sorted. The task is to find the median of the given matrix.


Example 1

Input: matrix=[ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 

Output: 5

Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5
"""
# brute approach using linear search of matrix traversal
# TC = O(R*C log(R*C)) and SC = O(R*C)
def medianMatrix(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            result.appen(matrix[i][j])
    result.sort()
    return result[(rows * cols)//2]
  
