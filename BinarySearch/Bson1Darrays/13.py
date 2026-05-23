# find peak element in array

"""
Docstring for BinarySearch.Bson1Darrays.13
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element,
and return its index. If the array contains multiple peaks, 
return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, 
an element is always considered to be strictly greater than a 
neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""


# extreme naive brute force using linear search
# TC = O(N) and SC = O(1)
def peaki(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(n):
        if nums[i] > largest:
            largest =  nums[i]
            index  = i
    return index


# brute force 
# TC = O(N) and SC = O(1)
def peak(nums):
    n = len(nums)
    if nums[0] > nums[1]:
        return 0
    for i in range(1,n-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i
    if nums[n-1] > nums[n-2]:
        return n-1
    
        
# optimal approach using binary search

def peakk(nums):
    n = len(nums)
    low = 0
    high = n-1
    while low < high:
        mid =low+(high-low)//2
        if nums[mid] < nums[mid+1]:
            low = mid+1
        else:
            high =  mid-1
    return low