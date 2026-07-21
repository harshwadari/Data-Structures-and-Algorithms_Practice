# 120. Triangle
"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 
on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total 
number of rows in the triangle?
"""


# Recursive appraoch using backtracking 
# TC = O(2^N) and SC = O(N)
def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        def backtrack(i,j):
            if i == rows - 1:
                return triangle[i][j]
            down = triangle[i][j] + backtrack(i+1,j)
            diagonal = triangle[i][j] + backtrack(i+1,j+1)
            return min(down,diagonal)
        return backtrack(0,0)


# Memoization Appraoch 
# TC = O(n²)  SC = O(n²) DP + O(n) recursion = O(n²)
def minimumTotal(self, triangle):
    rows = len(triangle)
    dp = [[-1] * rows for i in range(rows)]
    def backtrack(i,j):
        if i == rows - 1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        down = triangle[i][j] + backtrack(i+1,j)
        diagonal = triangle[i][j] + backtrack(i+1,j+1)
        dp[i][j] = min(down,diagonal)
        return dp[i][j]
    return backtrack(0,0)





# Tabultion Appraoch

# Tabulationn with space Optimization

# TC = O(N^2) and SC = O(N) dp space 
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        prev = [-1] * rows
        for i in range(rows):
            prev[i] = triangle[rows - 1][i]
        for i in range(rows-2,-1,-1):
            curr = [-1] * (i + 1)
            for j in range(0,i+1):
                down = triangle[i][j] + prev[j]
                diagonal = triangle[i][j] + prev[j+1]
                curr[j] = min(down,diagonal)
            prev = curr
        return prev[0]

