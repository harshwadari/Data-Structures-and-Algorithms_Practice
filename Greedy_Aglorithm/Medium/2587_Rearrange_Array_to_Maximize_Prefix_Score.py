# 2587. Rearrange Array to Maximize Prefix Score
"""
You are given a 0-indexed integer array nums. You can rearrange the elements of 
nums to any order (including the given order).

Let prefix be the array containing the prefix sums of nums after rearranging it. 
In other words, prefix[i] is the sum of the elements from 0 to i in nums after 
rearranging it. The score of nums is the number of positive integers in the array prefix.

Return the maximum score you can achieve.

 

Example 1:

Input: nums = [2,-1,0,1,-3,3,-3]
Output: 6
Explanation: We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.
Example 2:

Input: nums = [-2,-3,0]
Output: 0
Explanation: Any rearrangement of the array will result in a score of 0.
 

Constraints:

1 <= nums.length <= 105
-106 <= nums[i] <= 106
"""

# Brute Appraoch 
# TC = O(NlogN) + O(2N) and SC = O(N)
def brutemaxScore(nums:list[int]) -> int:
    nums.sort(reverse=True)
    maxScore = 0
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    for i in range(len(prefix)):
        if prefix[i] > 0:
            maxScore += 1
    return maxScore 


# Better Appraoch 
# TC = O(NlogN) + O(N) and SC = O(N)
def bettermaxScore(nums:list[int]) -> int:
    nums.sort(reverse=True)
    maxScore = 0
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    if prefix[0] > 0:
        score += 1
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
        if prefix[i] > 0:
            maxScore += 1
    return maxScore


# Optimal Appraoch 
# TC = O(NlogN)  + O(N) and SC = O(1)
def OptimalmaxScore(nums:list[int]) -> int:
    nums.sort(reverse=True)
    maxscore = 0
    prefix = 0
    for num in nums:
        if num > 0:
            prefix += num
            if prefix > 0:
                maxscore += 1
            else:
                break
    return maxscore 