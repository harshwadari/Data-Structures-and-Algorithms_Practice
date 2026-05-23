"""
Docstring for BinarySearch.6
S

34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing
order, find the starting and ending position of a given
target value.

If target is not found in the array, return [-1, -1].
"""

# brute Force method using linear search
# TC = O(N) and SC = O(1)

def searchrange(nums,target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(n):
        if nums[i] == target:
            if first ==-1:
                first = i
            last = i
    return [first,last]
print(searchrange([1,2,3,4,4,4,5,6,7],4))


#optimal method using binary search
# TC = O(logN) and SC = O(1)
def search(nums,target):
    n= len(nums)
    first = -1
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            if nums[mid] ==target:
                first = mid
            high = mid-1
        else:
            low = mid+1
    last = -1
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] <= target:
            if nums[mid] == target:
                last = mid
            low = mid+1
        else:
            high = mid-1
    return [first, last]
print(search([5,7,7,8,8,10],8))
