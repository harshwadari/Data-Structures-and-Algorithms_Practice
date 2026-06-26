# Indexes of Subarray Sum
"""
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
"""


# Brute force approach is using nested loops and checking first valid answer
# TC = O(N^2) and SC = O(1)
def indexessub(nums: list[int], target:int) -> list[int]:
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            if total == target:
                return [i + 1,j + 1]
    return -1

# Optimal appraoch using sliding window
# TC = O(2N) and SC = O(1)

def subarraySum(arr: list[int], target: int) -> list[int]:
    total = 0
    left = 0
    for right in range(len(arr)):
        total += arr[right]
        while total > target and left <= right:
            total -= arr[left]
        if total == target:
            return [left + 1,right + 1]
    return [-1]