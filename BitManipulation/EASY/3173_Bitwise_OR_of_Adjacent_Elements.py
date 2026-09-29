# 3173 — Bitwise OR of Adjacent Elements
"""

Given an array nums of length n, return an array answer of length n - 1 
such that answer[i] = nums[i] | nums[i + 1] where | is the bitwise OR operation

Example 1:
Input: nums = [1,3,7,15]

Output: [3,7,15]

Example 2:
Input: nums = [8,4,2]

Output: [12,6]

Constraints:
2 <= nums.length <= 100
0 <= nums[i] <= 100
"""



"""
Bitwise OR (|):
- Compares two numbers bit by bit.
- If either bit is 1, result is 1.
- If both bits are 0, result is 0.

Example:
5  = 101
3  = 011
OR = 111 = 7

Basically, OR combines the 1-bits of both numbers.

"""

# Optimal Appraoch using bitwise OR
# TC = O(N) and SC = O(N)
def bitwiseOR(nums):
    result = []
    for i in range(len(nums)-1):
        result.append(nums[i] | nums[i+1])
    return result