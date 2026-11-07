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




# Brute force appraoch using greedy 
# TC = O(N ^ 2) and SC = O(1)
class Solution(object):
    def minMoves(self, nums):
        def check(nums):
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    return False
            return True

        count = 0

        while not check(nums):
            index = nums.index(max(nums))

            for i in range(len(nums)):
                if i != index:
                    nums[i] += 1

            count += 1

        return count




# Otpimal Appraoch using math observation pattern
# TC = O(N) and SC = O(1)
# increasing n - 1 elements by one == decreasing one element by one.

def movesMin(nums:list[int]) -> int:
    mini = min(nums)
    moves = 0
    for num in nums:
        moves += num - mini
    return moves