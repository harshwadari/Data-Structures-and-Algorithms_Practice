# 3693. Climbing Stairs II
"""
You are climbing a staircase with n + 1 steps, numbered from 0 to n.

You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.

From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)2

You start from step 0 with cost = 0.

Return the minimum total cost to reach step n.

 

Example 1:

Input: n = 4, costs = [1,2,3,4]

Output: 13

Explanation:

One optimal path is 0 → 1 → 2 → 4

Jump	Cost Calculation	Cost
0 → 1	costs[1] + (1 - 0)2 = 1 + 1	2
1 → 2	costs[2] + (2 - 1)2 = 2 + 1	3
2 → 4	costs[4] + (4 - 2)2 = 4 + 4	8
Thus, the minimum total cost is 2 + 3 + 8 = 13

Example 2:

Input: n = 4, costs = [5,1,6,2]

Output: 11

Explanation:

One optimal path is 0 → 2 → 4

Jump	Cost Calculation	Cost
0 → 2	costs[2] + (2 - 0)2 = 1 + 4	5
2 → 4	costs[4] + (4 - 2)2 = 2 + 4	6
Thus, the minimum total cost is 5 + 6 = 11

Example 3:

Input: n = 3, costs = [9,8,3]

Output: 12

Explanation:

The optimal path is 0 → 3 with total cost = costs[3] + (3 - 0)2 = 3 + 9 = 12

 

Constraints:

1 <= n == costs.length <= 105​​​​​​​
1 <= costs[i] <= 104
"""
# Recursive Backtracking Appraoch 
# TC = O(3 ^N) and SC  =O(N)
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        def solve(i):
            if i == 0:
                return 0
            ans = float('inf')
            for j in range(1,4):
                if i - j >= 0:
                    mincost = solve(i-j) + costs[i-1] + j * j
                    if mincost < ans:
                        ans = mincost
            return ans
        return solve(n)


# memoization approach
# Tc = O(N) and SC = O(N) + O(N)
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [-1] * (n+1)
        def solve(i):
            if i == 0:
                return 0
            ans = float('inf')
            if dp[i] != -1:
                return dp[i]
            for j in range(1,4):
                if i - j >= 0:
                    mincost = solve(i-j) + costs[i-1] + j * j
                    if mincost < ans:
                        ans = mincost
            dp[i] = ans
            return dp[i]
        return solve(n)





# Tabulation bottom up  
# TC = O(3N) and SC = O(N)
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in range(1,4):
                if i - j >= 0:
                    mincost = dp[i-j] + costs[i-1] + j * j
                    if mincost < dp[i]:
                        dp[i] = mincost
        return dp[n]






# Tabulation with space optimization 
# TC = O(n) and SC = O(1)


class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')] * 4
        dp[0] = 0
        for i in range(1,n+1):
            ans = float('inf')
            for j in range(1,4):
                if i - j >= 0:
                    mincost = dp[(i-j) % 4] + costs[i-1] + j * j
                    if mincost < ans:
                        ans = mincost
            dp[i%4] = ans
        return dp[n%4]