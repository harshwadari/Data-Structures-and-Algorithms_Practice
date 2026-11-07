# 453. Minimum Moves to Equal Array Elements
"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
The answer is guaranteed to fit in a 32-bit integer.
"""

# Optimal Appraoch using sorting greedy 
# TC = O(NlogN) and SC = O(1)
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n % 2 != 0:
            median = nums[n // 2]
        else:
            median = (nums[n//2 - 1] + nums[n//2]) / 2
        moves = 0
        for i in range(n):
            moves += abs(nums[i] - median)
        return moves 