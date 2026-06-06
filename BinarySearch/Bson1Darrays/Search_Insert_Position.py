# Search insert position

"""
Docstring for BinarySearch.Bson1Darrays.4
Given a sorted array of nums consisting of distinct integers 
and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Example 1

Input: nums = [1, 3, 5, 6], target = 5
Output: 2
Explanation: The target value 5 is found at index 2 in the sorted 
array. Hence, the function returns 2
"""

# brute force method using linear search
# TC =  O(N) and SC = O(1)
def search(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] >= target:
            return i
    return n
print(search([1,3,5,6],2))


# optimal approach using binary search
# TC = O(logN) and SC = O(1)
def sein(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    lb = n
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >=target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
print(sein([1,3,5,6],2))
