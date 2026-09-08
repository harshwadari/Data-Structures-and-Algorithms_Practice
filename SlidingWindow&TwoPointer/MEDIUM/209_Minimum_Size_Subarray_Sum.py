# 209. Minimum Size Subarray Sum
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""


# Brute Force Appraoch by Generating all Subarrays and checking the answer
# TC = O(N ^ 2) and SC = O(1)
def minsubarrlen(nums:list[int],target:int) -> int:
    minlen = float('inf')
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            if total >= target:
                minlen = min(minlen,j - i +1)
    if minlen == float('inf'):
        return 0
    return minlen





# Optimal Appraoch using Sliding Window
# TC = O(N) and SC = O(1)
def Optimalminlensubarray(nums:list[int],target:int) -> int:
    minlen = 0
    total = 0
    left = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            minlen = min(minlen,right - left + 1)
            total -= nums[left]
            left += 1
    if minlen == float('inf'):
        return 0
    return minlen 