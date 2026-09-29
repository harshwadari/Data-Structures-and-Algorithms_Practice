# 477. Total Hamming Distance
"""
The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all 
the pairs of the integers in nums.

 

Example 1:

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Example 2:

Input: nums = [4,14,4]
Output: 4
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 109
The answer for the given input will fit in a 32-bit integer.
"""

# naive appraoch 
# TC = O(N ^ 2) and SC = O(1)
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def hamming(x,y):
            count = 0
            ans = x ^ y
            for i in range(32):
                if ans & (1 << i) != 0:
                    count += 1
            return count
        total = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                total += hamming(nums[i],nums[j])
                
        return total



# Optimal Appraoch 
# TC = O(N) and SC = O(1)
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(32):
            ones = 0
            for num in nums:
                if num & (1 << i) == 0:
                    ones += 1
            zeroes = n - ones
            total += zeroes * ones
        return total
    