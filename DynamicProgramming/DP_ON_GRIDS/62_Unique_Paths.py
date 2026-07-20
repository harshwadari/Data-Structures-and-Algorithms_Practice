# 62. Unique Paths
"""
There is a robot on an m x n grid. The robot is initially located at the top-left c
orner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner 
(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the 
bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
"""
# TC = O(2^(M*N)) and SC = O(M*N) stack space
# Recursive Approach using backtacking 
def paths(m,n):
    def backtrack(i,j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0 :
            return 0
        up = backtrack(i-1,j)
        left = backtrack(i,j-1)
        return up + left
    return backtrack(m-1,n-1)
print(paths(3,7))


# Memoization Approach
# TC = O(M*N) and SC = O(M*N) dp space and O(M+N) Stack Space
def memoPaths(m,n):
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    def backtrack(i,j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        up = backtrack(i-1,j)
        left = backtrack(i,j-1)
        dp[i][j] = up + left
        return dp[i][j]
    return backtrack(m-1,n-1)
print(memoPaths(3,7))


# Tabulation Appraoch
# TC = O(M*N) and SC = O(M*N)

def uniquePaths(self, m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
                continue
            up = dp[i-1][j]
            left = dp[i][j-1]
            dp[i][j] = up + left
    return dp[m-1][n-1]


# Tabulation with Space Optimization
# TC = O(M*N) and SC = O(N) 

def UniquePaths(m:int,n:int) -> int:
    prev = [0] *n
    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr[0] = 1
            else:
                if i > 0:
                    up = prev[j]
                else:
                    up = 0
                if j > 0:
                    left = curr[j-1]
                else:
                    left = 0
                curr[j] = up + left
        prev = curr
    return prev[n-1]


# Optimal differnt appraoch using combination math formula
# TC = O(min(m,n)) and SC = O(1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = m + n - 2
        r = min(m - 1, n - 1)
        ans = 1
        for i in range(1, r + 1):
            ans = ans * (N - r + i) // i
        return ans