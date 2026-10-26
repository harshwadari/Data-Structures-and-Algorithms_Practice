# 377. Combination Sum IV
"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? 
How does it change the problem? What limitation 
we need to add to the question to allow negative numbers?
"""

# Recursive Backtracking Approach
# TC = O(2^N) and SC = O(N)
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def backtrack(index,target):
            if target == 0:
                return 1
            if index >= len(nums) or  target < 0:
                return 0
            pick = backtrack(0,target - nums[index])
            notpick = backtrack(index+1,target)
            return pick + notpick
        return backtrack(0,target)



# Memoization
"""
Memoization Complexity:

| Time Complexity  | O(n * target) |
| Space Complexity | O(n * target) |
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n)]
        def backtrack(index,target):
            if target == 0:
                return 1
            if index >= len(nums) or  target < 0:
                return 0
            if dp[index][target] != -1:
                return dp[index][target]
            pick = backtrack(0,target - nums[index])
            notpick = backtrack(index+1,target)
            dp[index][target] = pick + notpick
            return dp[index][target]
        return backtrack(0,target)


# bottom up tabulation solution 
# TC = O(n* target) and SC = O(n* target)
class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1

        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]

        return dp[target]