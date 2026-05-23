# Single Number 
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1
"""

# brute approach using hashing
# TC = O(2N) and SC = O(N)
def singlenum(nums):
    map = {}
    for i in range(len(nums)):
        if nums[i] in map:
            map[nums[i]] +=1
        else:
            map[nums[i]] = 1
    for val, freq in map.items():
        if freq == 1:
            return val
        

# even better approach using math trick
# TC = O(N) and SC= O(N)
def single(nums):
    return 2 * sum(set(nums)) - sum(nums)

# optimal approach using bit manipulation 
