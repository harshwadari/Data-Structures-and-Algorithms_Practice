# 3737. Count Subarrays With Majority Element I
"""
You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

 

Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.
"""


# Brute force approac by generating all subarrays and checking majority element
# TC = O(N^2) and SC = O(1)
def subarray(nums: list[int],target: int) ->int:
    count = 0
    for i in range(len(nums)):
        freq = 0
        for j in range(i,len(nums)):
            if nums[j] == target:
                freq += 1
            length = j - i + 1
            if freq > length // 2:
                count += 1
    return count

# Otpimal appraoch