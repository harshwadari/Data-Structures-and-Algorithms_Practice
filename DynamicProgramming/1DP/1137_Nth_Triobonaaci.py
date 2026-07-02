# 1137. N-th Tribonacci Number
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
# Recursive approach 
# TC = O(N^3) and SC = O(N) where N is stack space 
def tribo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)


# Memoization approach 
# TC = O(N) and SC = O(N) + O(N)
def tribomemo(n):
    dp = [-1] * (n + 1)
    def solve(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = solve(n - 1) + solve(n - 2) + solve(n - 3)
        return dp[n]
    return solve(n)

# Tabulation appraoch 
# TC = O(N) and SC = O(N)
def tabtribo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

# Tabulation with space Optimization 
# TC = O(N) and SC = O(1)
def tabspacetribo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    prev3 = 0
    prev2 = 1
    prev1 = 1
    for i in range(3,n+1):
        curr = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = curr
    return prev1
