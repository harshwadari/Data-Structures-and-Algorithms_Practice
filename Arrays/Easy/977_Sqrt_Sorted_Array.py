# 977. Squares of a Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

# bettter opproach using sorting 
# TC = O(NlogN) and SC = O(1)
def sqrt(nums:list[int])  ->list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    nums.sort()
    return nums

# Optimal appraoch using two pointer 
# TC = O(N) and SC = O(1)
def twosqrt(nums:list[int]) ->list[int] :
    n = len(nums)
    left = 0
    right = n - 1
    result = [0] * n
    for i in range(n - 1,-1,-1):
        if abs(nums[left]) > abs(nums[right]):
            value = nums[left]
            left += 1
        else:
            value = nums[right]
            right -= 1
        result[i] = value ** 2
    return result 