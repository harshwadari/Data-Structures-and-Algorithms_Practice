# Search in a sorted rotated array

"""
Docstring for BinarySearch.Bson1Darrays.8
Given an integer array nums, sorted in ascending order 
(with distinct values) and a target value k. The array is rotated 
at some pivot point that is unknown. Find the index at which k is 
present and if k is not present return -1.

Example 1

Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output: 4
Explanation: Here, the target is 0. We can see that 0 is present 
in the given rotated sorted array, nums. Thus, we get output as 4,
 which is the index at which 0 is present in the array.
"""


# brute approach using linear search 
# TC = O(N) and SC = O(1)
def searchrot(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1




# optimal approach using binary searc
# TC + O(logN) and SC = O(1)

def binsearchrot(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1
    return -1

        