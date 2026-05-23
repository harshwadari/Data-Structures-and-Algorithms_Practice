#Search in matrix 2
"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
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

# better approach using binary search
# TC = O(M*logN) and SC = O(1)
# Key Idea:
# For each row, apply binary search to find the target.
def matrxiSearchBetter(matrix : list[list[int]],target : int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        low = 0
        high = cols -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                low = mid + 1
            else:
                high = mid -1
    return False




# optimal approach using binary search
# TC = O(M+N) and SC = O(1)
# Key Idea:
# Start from the top-right corner of the matrix and eliminate rows or columns based on comparisons.
def matrxiSearchOptimal(matrix : list[list[int]],target : int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols -1
    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i +=1
        else:
            j -=1
    return False