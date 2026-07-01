# Frog Jump
"""
Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the last stair. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the last stair.

Example:

Input: heights[] = [20, 30, 40, 20]
Output: 20
Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10
jump from stair 1 to 3: cost = |20 - 30| = 10
Total Cost = 10 + 10 = 20
"""
# fist approach using Recursion
# TC = O(2^N) and SC = O(N) where n is stack space
def minCost(height):
        # code here
        n = len(height)
        def backtrack(index):
            if index == 0:
                return 0
            jump1 = backtrack(index - 1) + abs(height[index] - height[index - 1])
            if index > 1:
                jump2 = backtrack(index - 2) + abs(height[index] - height[index - 2])
            else:
                jump2 = float('inf')
            return min(jump1,jump2)
        return backtrack(n-1)

# better appoach using memoization 
# TC = O(N) and SC = O(N) stack space + O(N) dp array
def jump(height):
    n = len(height)
    dp = [-1] * n
    def backtrack(index):
        if index == 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        jump1 = backtrack(index - 1) + abs(height[index] - height[index - 1])
        if index > 1:
            jump2 = backtrack(index - 2) + abs(height[index] - height[index - 2])
        else:
            jump2 = float('inf')
        dp[index] =  min(jump1,jump2)
        return dp[index]
    return backtrack(n-1)
        

# Tabulation approach 
# TC = O(n) and SC = O(N) dp arr space
def minCost(self, height):
        # code here
        n = len(height)
        dp = [-1] * n
        dp[0] = 0
        for index in range(1,n):
            jump1 = dp[index - 1] + abs(height[index] - height[index - 1])
            if index > 1:
                jump2 = dp[index - 2] + abs(height[index] - height[index - 2])
            else:
                jump2 = float('inf')
            dp[index] =min(jump1,jump2)
        return dp[n - 1]
    

# Most optimal approach usnig tabulation  with space optimization 
# TC = O(N) and SC = O(1)
def frogy(arr):
    prev2 = 0
    prev1 = 0
    for  i in range(1,len(arr)):
         pass