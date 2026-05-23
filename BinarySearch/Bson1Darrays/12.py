# to find single element in a sorted array

"""
Docstring for BinarySearch.Bson1Darrays.12

You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one 
element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.


Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""


# binary search is used to reduce search space 

# brute force method 
# TC = O(N) and SC = O(1)
def single(nums):
    for i in range(len(nums)):
        if nums[i-1] != nums[i] != nums[i+1]:
            return nums[i]
    