# 198. House Robber
"""
You are a professional robber planning to rob houses along a 
street. Each house has a certain amount of money stashed, the only 
constraint stopping you from robbing each of them is that adjacent 
houses have security systems connected and it will automatically contact 
the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

# Recursive approach 
# TC = (2^N) and SC = O(N)
def rob(nums):
        n = len(nums)
        def backtrack(index):
            if index == 0:
                return nums[index]
            if index < 0:
                return  0
            pick = nums[index] + backtrack(index - 2)
            notpick = 0 + backtrack(index - 1)
            return max(pick,notpick)
        return backtrack(n-1)

# memoization approach 
# TC = O(N) and SC = O(N) stack space + O(N) dp array space 
def rob(self, nums):
        n = len(nums)
        dp = [-1] * n
        def backtrack(index):
            if index == 0:
                return nums[index]
            if index < 0:
                return  0
            if dp[index] != -1:
                return dp[index]
            pick = nums[index] + backtrack(index - 2)
            notpick = 0 + backtrack(index - 1)
            dp[index] =  max(pick,notpick)
            return dp[index]
        return backtrack(n-1)


# tabulation approach 
# TC = O(N) and SC = O(N)
def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if i > 1:
                pick = nums[i] + dp[i -2]
            else:
                pick = nums[i]
            notpick = 0 + dp[i - 1]
            dp[i] = max(pick,notpick)
        return dp[len(nums) - 1]

# Tabulation apporach with space optimization
# TC = O(N) and SC = O(1)
def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = nums[0]
        prev2 = 0
        for i in range(1,len(nums)):
            if i > 1:
                pick = nums[i] + prev2
            else:
                pick = nums[i]
            notpick = 0 + prev1
            curr = max(pick,notpick)
            prev2 = prev1
            prev1 = curr
        return  prev1