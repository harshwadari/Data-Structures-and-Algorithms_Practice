# Find row with maximum 1's

"""
Brute Force Intuition

Think in the most straightforward way possible:

For every row

Count how many 1s exist in that row

Keep track of:

maximum count of 1s

index of that row

Return the row index having the maximum ones.

So basically:

row → count ones → compare with max → update
"""
# brute approach using linear search of matrix traversal
# TC = O(M*N) and SC = O(1)
def rowWithMax1s(matrix : list[list[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    max_ones = 0
    row_index = -1
    for i in range(rows):
        count_ones = 0
        for j in range(cols):
            if matrix[i][j] == 1:
                count_ones += 1
        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i
    return row_index


# better approach using binary search
# TC = O(M*logN) and SC = O(1)
# Key Idea:
# Since each row is sorted, we can use binary search to find the first occurrence of
# 1 in each row, which will give us the count of 1s in that row.
def rowWithMax1sBetter(matrix : list[list[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    max_ones = 0
    row_index = -1
    for i in range(rows):
        low = 0
        high = cols -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[i][mid] == 1:
                high = mid -1
            else:
                low = mid + 1
        count_ones = cols - low
        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i
    return row_index

# optimal approach 
# TC = O(M+N) and SC = O(1)
# Key Idea:
# Start from the top-right corner of the matrix and move left if you encounter a 1, or move down if you encounter a 0. This way, you can find the row with the maximum number of 1s in a single pass.

def rowWithMax1s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols - 1
    row_index = -1

    while i < rows and j >= 0:

        if matrix[i][j] == 1:
            row_index = i
            j -= 1
        else:
            i += 1

    return row_index