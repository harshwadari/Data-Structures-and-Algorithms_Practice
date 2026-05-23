#1848. Minimum Distance to the Target Element

"""
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that 
nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
Return abs(i - start).

It is guaranteed that target exists in nums.

Example 1:

Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
"""


# Optimal Appraoch using Linear Search

# TC = O(N) and SC = O(1)

def getminDist(nums,target,start):
    n = len(nums)
    minDistance = float('inf')
    for i in range(n):
        if nums[i] == target:
            distance = abs(i - target)
            minDistance = min(minDistance , distance)
    return minDistance