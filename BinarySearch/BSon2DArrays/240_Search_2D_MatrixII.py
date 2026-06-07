# 240. Search a 2D Matrix II

# better approach using linear search
# TC = O(N*M) where n is rows and m is cols and SC = O(1) 
"""
if matrix is square tc will be N^2
"""

def searchMatrix(mat : list[list[int]],target : int) -> bool:
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == target:
                return True
    return False
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

# optimal approach using binary Search
# TC = O(log(m*n)) and SC = O(1)

def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = cols - 1
        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i +=1
            else:
                j -=1
        return False
