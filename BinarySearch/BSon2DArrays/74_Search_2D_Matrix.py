# 74. Search a 2D Matrix

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


# optimal appraoch using binary search on matrix
# TC = O(log(M*N)) and SC = O(1)

def bsSearchMatrix(mat,target):
    low = 0
    high = len(mat) - 1
    rows = len(mat)
    cols = len(mat[0])
    while low <= high:
        mid = (low + high) // 2
        row = mid//cols
        col = mid%cols
        if mat[row][col]== target:
            return [row,col]
        elif mat[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
print(bsSearchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))