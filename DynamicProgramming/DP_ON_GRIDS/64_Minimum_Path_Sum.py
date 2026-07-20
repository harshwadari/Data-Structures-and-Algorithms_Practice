# 64. Minimum Path Sum
"""
Given a m x n grid filled with non-negative numbers, find a path from top 
left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


# # Recursive Appraoch using backtracking 
# TC = O(2^i*j) where i and j is rows and cols SC = O(i + j) stack space
def minsumpath(grid:list[list[int]]) -> int:
    i = len(grid)
    j = len(grid[0])
    def backtrack(i,j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        left = backtrack(i,j-1)
        up = backtrack(i-1,j)
        return grid[i][j] + min(left,up)
    return backtrack(i-1,j-1)







# Memoization Appraoch 
# TC = O(i *j) and SC = O(i * j ) dp array + O(i +j) stack space
def minmemopathsum(grid):
    i = len(grid)
    j = len(grid[0])
    dp = [[-1 for _ in range(j)] for _ in range(i)]
    def backtrack(i,j):
        if i == 0 and j == 0:
            return grid[i][j]
        if i < 0 or j < 0:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        left = backtrack(i,j-1)
        up = backtrack(i-1,j)
        dp[i][j] = grid[i][j] + min(left,up)
        return dp[i][j]
    return backtrack(i-1,j-1)





# Tabulation Appraoch 
# TC = O(i * j) and SC = O(i * j)
def minpath(grid):
    m = len(grid)
    n = len(grid[0])
    dp[0][0] = grid[0][0]
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    for  i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                up = float('inf')
            else:
                up = dp[i-1][j]
            if j == 0:
                left = float('inf')
            else:
                left = dp[i][j-1]
            dp[i][j] = grid[i][j] + min(up,left)
    return dp[m-1][n-1]





# Tabulation with Space Optimization
# TC = O(i * j) and SC = O(N)

def optimalminspace(grid):
    m = len(grid)
    n = len(grid[0])
    prev = [0] * n
    for  i in range(m):
        curr = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr[0] = grid[0][0]
                continue
            if i == 0:
                up = float('inf')
            else:
                up = prev[j]
            if j == 0:
                left = float('inf')
            else:
                left = curr[j-1]
            curr[j]= grid[i][j] + min(up,left)
        prev = curr
    return prev[n-1]