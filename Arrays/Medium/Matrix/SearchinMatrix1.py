# 74. Search a 2D Matrix
"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

# brute approach using linear search of matrix traversal
# TC = O(M*N) and SC = O(1)
def matrxiSearch(matrix : list[list[int]],target : int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False
print(matrxiSearch([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

# optimal approach using binary search
# TC = O(log(M*N)) and SC = O(1)

# Key Idea:
# Treat the 2D matrix as a flattened sorted array and apply binary search using index mapping.
def matrxiSearchOptimal(matrix : list[list[int]],target : int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0
    high = rows*cols -1
    while low <= high:
        mid = (low + high) // 2
        mid_value = matrix[mid//cols][mid%cols]
        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid -1
    return False
print(matrxiSearchOptimal([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
