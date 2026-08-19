# 523. Continuous Subarray Sum
"""
Given an integer array nums and an integer k, return true if nums has a 
good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0
 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
 

"""


# Brute Force Appraoch by generating all subarrays and check condition
# TC = O(N ^ 2) and SC = O(1)
def brutecheckSum(nums,k):
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            if j - i + 1 >= 2:
                if total % k == 0:
                    return True
    return False




# Relization Appraoch thinking that sliding window 
# will work because my dumbass brain thought of sliding windlow by seeing subarray
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            if right - left + 1 >= 2:
                if total % k == 0:
                    return True
                total -= nums[left]
                left += 1
        return False

"""
This approach will not work because the condition lenght of subbarray can be 
greater or equal to 2 but sliding window will shrink at each iteration making
the size of subarray at lenght 2 only sot that makes no use of using this appraoch 
"""


# Optimal Appraoch using prefixsum and hashmap
# TC = O(N) and SC  = O(N) 
def OptimalSubarraySum(nums:list[int],k:int) -> bool:
    freq = {0:-1}
    prefixSum = 0
    for i in range(len(nums)):
        prefixSum += nums[i]
        remainder = prefixSum % k
        if remainder in freq:
            if i - freq[remainder] >= 2:
                return True
        else:
            freq[remainder] = i
    return False