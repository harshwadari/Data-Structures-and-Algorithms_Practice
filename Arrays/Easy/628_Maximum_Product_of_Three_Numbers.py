# 628. Maximum Product of Three Numbers
"""
You are given an integer array nums.

Find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,-3]

Output: -6

Explanation:

The only three numbers are 1, 2, and -3, so the maximum product is 1 * 2 * -3 = -6.

Example 2:

Input: nums = [1,2,3,4]

Output: 24

Explanation:

The largest product comes from the three greatest numbers: 2 * 3 * 4 = 24.

Example 3:

Input: nums = [-1,-2,-3]

Output: -6

Explanation:

The only three numbers are -1, -2, and -3, so the maximum product is (-1) * (-2) * (-3) = -6.

 

Constraints:

63 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""


# Optimal Approach using Greedy and Sorting
# TC = O(NlogN) and SC = O(1)
def product(nums):
    nums.sort()
    ans1 = nums[-1] * nums[-2] * nums[-3]
    ans2 = nums[0] * nums[1] * nums[-1]
    return max(ans1,ans2)
