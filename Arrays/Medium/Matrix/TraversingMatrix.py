# matrix traversing
# TC = O(N^2) and SC = O(1)
def matrix(nums:list[list[int]]):
    n = len(nums)
    rows = n
    columns = len(nums[0])
    for i in range(rows):
        for j in range(columns):
            print(nums[i][j],end=" ")
        print()
print(matrix([[1,2,3],[4,5,6],[7,8,9]]))



# printing upper triangle of a matrix or a 2d array/list

def upperTriangleMatrix(nums:list[list[int]]):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(rows):
        for j in range(cols):
            if j >= i:# index manipulation 
                print(nums[i][j], end = " ")
            else:
                print("*", end=" ")
        print()
print(upperTriangleMatrix([[1,2,3],[4,5,6],[7,8,9]]))



# printing lower triangle of a matrix or a 2d array/list

def lowerTriangleMatrix(nums:list[list[int]]):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(rows):
        for j in range(cols):
            if i >=j: # index manipulation 
                print(nums[i][j], end = " ")
            else:
                print("*", end=" ")
        print()
print(lowerTriangleMatrix([[1,2,3],[4,5,6],[7,8,9]]))




# print diagonal of matrix


def diagonalofMatrix(nums:list[list[int]]):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(rows):
        for j in range(cols):
            if i == j: # index manipulation 
                print(nums[i][j], end = " ")
            else:
                print("*", end=" ")
        print()
print(diagonalofMatrix([[1,2,3],[4,5,6],[7,8,9]]))


# matrix transpose

def MatrixTranspose(nums:list[list[int]]):
    rows = len(nums)
    cols = len(nums[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]
    print(result,end=" \n")
    
print(MatrixTranspose([[1,2,3],[4,5,6],[7,8,9]]))