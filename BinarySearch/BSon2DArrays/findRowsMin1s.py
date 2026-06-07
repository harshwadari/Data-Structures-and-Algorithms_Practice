# Find row with maximum 1's

# brute / better approach using linear search

# TC = O(N*M) and SC = O(1)
def rowWithMax1s( mat):
        rows = len(mat)
        cols = len(mat[0])
        maxcount = 0
        rowindex = -1
        for i in range(rows):
            count = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    count +=1
            if count > maxcount:
                maxcount = count
                rowindex = i
        return rowindex


# Optimal appraoch using binary search

def rowWithMax1s(self, arr):
        # code here
        rows = len(arr)
        cols = len(arr[0])
        maxOnes = 0
        result = -1
        for i in range(rows):
            low = 0
            high = cols - 1
            first = cols
            while low <= high:
                mid = (low + high) // 2
                if arr[i][mid] >= 1:
                    first = mid
                    high = mid -1
                else:
                    low = mid + 1
            ones = cols - first
            if ones > maxOnes:
                maxOnes = ones
                result = i
        return result
     