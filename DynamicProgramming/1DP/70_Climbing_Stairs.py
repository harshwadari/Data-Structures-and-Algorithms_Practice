# 70. Climbing Stairs
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
# This Question is full same as finbonaaci
# using recurion 
# TC = O(2^N) and SC = O(N) stack space

def fibb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibb(n-1) + fibb(n - 2)

# better appraoch using db memoizatioin 
# TC = O(N) and SC = O(N) + O(N)
def dpfib(n,dp):
    if  n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = dpfib(n-1) + dpfib(n -2)
    return dp[n]


# Tabulation bottom up approach 
# TC = O(N) and SC = O(N)
def tabfib(n):
    if n <= 1:
        return n
    dp = [-1] * n
    dp[0] = 0
    dp[1] = 1
    for i in range(n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# Tabulation with space Optimization 
# TC = O(N) and SC = O(1)
def spacefib(n):
    if n <= 1:
        return n
    prev2 = 0
    prev1 = 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


