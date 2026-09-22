# 897. Sum of Array Elements II
"""
Given an array nums, find the sum of elements of array using recursion.

Example 1:
Input : nums = [1, 2, 3]

Output : 6

Explanation : The sum of elements of array is 1 + 2 + 3 => 6.

Example 2:
Input : nums = [5, 8, 1]

Output : 14

Explanation : The sum of elements of array is 5 + 8 + 1 => 14.



Constraints:
1 <= n <= 100
0 <= nums[i] <= 100
"""
# TC = O(N) and SC = O(N) stack space 
class Solution:
    def arraySum(self, nums):
        #your code goes here
        def re(index):
            if index <  0:
                return 0
            return nums[index] + re(index-1)
        return re(len(nums)-1)