# 485. Max Consecutive Ones
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
# TC = O(N) and SC = O(1)

def maxOnes(nums):
    n = len(nums)
    count = 0
    maxcount = 0
    for i in range(n):
        if nums[i] == 1:
            count +=1
        else:
            maxcount = max(maxcount , count)
            count = 0
    return max(maxcount , count)



# different variation

def maxONes(nums):
    n = len(nums)
    count = 0
    maxcount = 0
    for i in range(n):
        if nums[i] == 1:
            count +=1
            maxcount = max(maxcount,count)
        else:
            count = 0
    return maxcount