# 213. House Robber II
"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are 
arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

#  Recursive appraoch
# TC = O(2^N) and SC = O(N)
class Solution(object):
    def backtrack(self,index,nums):
            if index == 0:
                return nums[index]
            if index < 0:
                return  0
            pick = nums[index] + self.backtrack(index - 2,nums)
            notpick = 0 + self.backtrack(index - 1,nums)
            return max(pick,notpick)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = self.backtrack(n - 2,nums[0:-1])
        ans2 = self.backtrack(n - 2,nums[1:n])
        return max(ans1,ans2)
    


# memoization approach 
# TC = O(N) and SC = O(N) + O(N)
class Solution(object):
    def backtrack(self,index,nums,dp):
            if index == 0:
                return nums[index]
            if index < 0:
                return  0
            if dp[index] != -1:
                return dp[index]
            pick = nums[index] + self.backtrack(index - 2,nums,dp)
            notpick = 0 + self.backtrack(index - 1,nums,dp)
            dp[index] =  max(pick,notpick)
            return dp[index]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * (n - 1)
        if n == 1:
            return nums[0]
        ans1 = self.backtrack(n - 2,nums[0:-1],dp)
        dp = [-1] * (n - 1) 
        ans2 = self.backtrack(n - 2,nums[1:n],dp)
        return max(ans1,ans2)
        


# Tabulation approach
# TC = O(N) and SC = O(N)
class Solution(object):
    def backtrack(self,nums):
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        for i in range(1,n):
            if i > 1:
                pick = nums[i] + dp[i - 2]
            else:
                pick = nums[i]
            notpick = 0 + dp[i - 1]
            dp[i] = max(pick,notpick)
        return dp[n - 1]
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = self.backtrack(nums[0:n-1])
        ans2 = self.backtrack(nums[1:n])
        return max(ans1,ans2)
    


# Tabulation with space Optimization
# TC = O(N) and SC = O(1)
class Solution(object):
    def backtrack(self,nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1,n):
            if i > 1:
                pick = nums[i] + prev2
            else:
                pick = nums[i]
            notpick = 0 + prev
            curr = max(pick,notpick)
            prev2 = prev
            prev = curr
        return prev
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = self.backtrack(nums[0:n-1])
        ans2 = self.backtrack(nums[1:n])
        return max(ans1,ans2)