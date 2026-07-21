# 63. Unique Paths II
"""
You are given an m x n integer array grid. There is a robot initially located 
at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any 
point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot 
takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right 
corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right



Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


# Recursive Appraoch Using Backtracking
# TC = O(2^i * j) and SC = O(i+j) stack space
def path(grid):
    i = len(grid)
    j = len(grid[0])
    def backtrack(i,j):
        if grid[i][j] == 1:
            return 0
        if i < 0 or j < 0 :
            return 0
        if i == 0 and j == 0:
            return 1
        left = backtrack(i,j-1)
        up = backtrack(i-1,j)
        return up + left
    return backtrack(i-1,j-1)




# Memoization Appraoch
# TC = O(i*j) and SC = O(i +j) stack space + O(i*j) dp space
def memopath(grid):
    i = len(grid)
    j = len(grid[0])
    dp = [[-1 for _ in range(j)] for _ in range(i)]
    def backtrack(i,j):
        if grid[i][j] == 1:
            return 0
        if i < 0 or j < 0 :
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        left = backtrack(i,j-1)
        up = backtrack(i-1,j)
        dp [i][j]= left + up
        return dp[i][j]
    return backtrack(i-1,j-1)



# Tabulation Appraoch
# TC = O(i*j) and SC =  O(i*j) dp space
def tabpath(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    if grid[i][j] == 1:
        return 0
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            left = 0
            up = 0
            if i > 0:
                up = dp[i-1][j]
            if j > 0:
                left = dp[i][j-1]
            dp[i][j] = left + up
    return dp[i-1][j-1]


# Tabulation with space Optimization
# TC = O(i * j) and SC = O(N)
class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        prev = [0] * n
        if grid[0][0] == 1:
            return 0
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                    continue
                if grid[i][j] == 1:
                    curr[j] = 0
                    continue
                up = 0
                left = 0
                if i > 0:
                    up = prev[j]
                if j > 0:
                    left = curr[j-1]
                curr[j] = up + left
            prev = curr
        return prev[n-1]   