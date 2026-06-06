# Implement upper Bound

"""
Docstring for BinarySearch.Bson1Darrays.3
upper bound is smallest index which is nums[i] > target
upper bound is the first occurrence of element greater than target in the sorted array
if target is not present in the array then it will return the index of the next greater element
Example 1
Input: nums = [1,2,2,3,3,3,4,5], target = 3
Output: 6
"""
# Tc = O(logN) and SC = O(1)
def upperBound (nums,target):
    n = len(nums)
    low = 0
    high = n-1
    up= n
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            up = mid
            high = mid-1
        else:
            low  = mid+1
    return up