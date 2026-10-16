# 456. 132 Pattern
"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
"""

# extreme Naive appraoch by generating and using three nested loops
# TC = O(N ^ 3) and SC = O(1)
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pattern is for every middle element nums[j]
        # i have to find smallest element less than nums[j]
        # and in right side of nums[j] smaller than nums[j] but
        # larger than nums[i] on left 
        # min(left) < nums[middle(j)] < nums[middle] and > nums[left]
        n = len(nums)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i < j < k and nums[i] < nums[k] < nums[j]:
                        return True
        return False



# Better Appraoch 
# TC = O(N ^ 2) and SC = O(1)
class Solution(object):
    def find132pattern(self, nums):
        n = len(nums)
        i = nums[0]
        for j in range(n):
            i = min(i,nums[j])
            for k in range(j+1,n):
                if i < nums[k] and nums[k] < nums[j]:
                    return True
        return False


# Optimal Appraoch using Monotonic Stack
# TC = O(N) and SC = O(N)
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pattern is for every middle element nums[j]
        # i have to find smallest element less than nums[j]
        # and in right side of nums[j] smaller than nums[j] but
        # larger than nums[i] on left 
        # min(left) < nums[middle(j)] < nums[middle] and > nums[left]
        stack = []
        third = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if third > nums[i]:
                return True
            while len(stack) != 0 and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])
        return False