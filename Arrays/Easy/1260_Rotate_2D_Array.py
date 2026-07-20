# 1260. Shift 2D Grid
"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""

# Brute approach flatter 2d array into 2d array apply rever rotate algo and build a new resutl mat

"""
TC is O(R *C + R * C + O(N)) whrer r is rows and c is col of given matrix  
and SC = O(N) where N is lenth of flatttened array
"""
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])
        k = k % len(nums)
        n = len(nums)
        def reve(left,right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1
    
        reve(0,n-1)
        reve(0,k-1)
        reve(k,n-1)
        idx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = nums[idx]
                idx += 1
        return grid
    

# Optimal appraoch using index manipulation 
"""
Idea

Treat the matrix as a 1D array.

For every cell (i, j):

Convert it to a 1D index.
Shift that index by k.
Convert the new index back to (row, col).
"""