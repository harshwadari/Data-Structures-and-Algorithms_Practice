# 1901. Find a Peak Element II
"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
"""
# brute approach using linear search of matrix traversal
# TC = O(M*N) and SC = O(1)
def findPeakGrid(matrix : list[list[int]]) -> list[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    maxi = matrix[0][0]
    r = 0
    c = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > maxi:
                maxi = matrix[i][j]
                r = i
                c = j
    return [r,c]


"""
Core Idea

Pick middle column

Find max element in that column

Compare it with left and right neighbor

Move toward the larger neighbor

If both neighbors are smaller → peak found
"""
# Key Idea:
# Binary search on columns combined with finding the global maximum in the current row to guide direction.

# optimal approach using binary search
# TC = O(M*logN) and SC = O(1)
def findPeakGridOptimal(matrix : list[list[int]]) -> list[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0
    high = cols -1
    while low <= high:
        mid = (low + high) // 2
        # Find the maximum element in the middle column
        max_row = 0
        for i in range(1, rows):
            if matrix[i][mid] > matrix[max_row][mid]:
                max_row = i
        # Compare with left and right neighbors
        left_neighbor = matrix[max_row][mid -1] if mid -1 >= 0 else float('-inf')
        right_neighbor = matrix[max_row][mid +1] if mid +1 < cols else float('-inf')
        
        if matrix[max_row][mid] > left_neighbor and matrix[max_row][mid] > right_neighbor:
            return [max_row, mid]
        elif left_neighbor > matrix[max_row][mid]:
            high = mid -1
        else:
            low = mid +1
    return [-1,-1]  # This line should never be reached due to problem constraints.
print(findPeakGridOptimal([[1,4],[3,2]]))  # Output: [0,1]