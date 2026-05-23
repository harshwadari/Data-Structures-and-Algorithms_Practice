# Search is rotated sorted array 2

"""
Docstring for BinarySearch.Bson1Darrays.9
Given an integer array nums, sorted in ascending order
 (may contain duplicate values) and a target value k. Now 
 the array is rotated at some pivot point unknown to you.
   Return True if k is present and otherwise, return False.

Example 1

Input : nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Output: True
Explanation: The element 3 is present in the array. So, the answer is True.
"""

#brute force appraoch using linear search
# TC = O(N) and SC = O(1)

def searchrot2(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return True
    return False


# optimal appraoch using binary search 
# TC = (logN) and SC = O(1)

def binsearcrot2(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        