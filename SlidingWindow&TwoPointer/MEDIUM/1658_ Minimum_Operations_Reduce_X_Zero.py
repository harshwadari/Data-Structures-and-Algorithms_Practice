# 1658. Minimum Operations to Reduce X to Zero
"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the 
first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""

# Optimal Appraoch using sliding windoew
# TC = O(N) and SC = O(1)
def MinOps(nums:list[int],k:int) -> int:
    n = len(nums)
    maxlen = -1
    total = sum(nums) - k
    if total == 0:
        return n
    if total < 0:
        return -1
    left = 0
    currsum = 0
    for right in range(n):
        currsum += nums[right]
        while currsum > total:
            currsum -= nums[left]
            left += 1
        if currsum == total:
            maxlen = max(maxlen, right - left + 1)
    if maxlen == -1:
        return -1
    return n - maxlen