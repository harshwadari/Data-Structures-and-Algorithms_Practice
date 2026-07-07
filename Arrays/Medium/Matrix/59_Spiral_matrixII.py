# 59. Spiral Matrix II
"""
Given a positive integer n, generate an n x n matrix filled with
elements from 1 to n2 in spiral order
"""
# TC = O(N^2) and SC = O(N^2)
def generateMatrix(n:int)->list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    top ,left = 0,0
    bottom = n - 1
    val = 1
    right = n - 1
    while left <= right:
        for i in range(left,right + 1):
            matrix[top][i] = val
            val += 1
        top += 1
        for i in range(top,bottom + 1):
            matrix[i][right] = val
            val += 1
        right -= 1
        for i in range(right,left - 1,-1):
            matrix[bottom][i] = val
            val += 1
        bottom -= 1
        for i in range(bottom,top - 1,-1):
            matrix[i][left] = val
            val += 1
        left += 1
    return matrix