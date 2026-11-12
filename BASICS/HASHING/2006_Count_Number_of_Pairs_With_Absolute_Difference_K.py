# 2006. Count Number of Pairs With Absolute Difference K
"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""


# Brute naive approach
# TC = O(N^2) and SC = O(1)
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count



# Optimal Approach using hashing 
"""
abs [x-y] = k 
rearraning : y = x - k and y = x + k
"""
# TC = O(N) and SC = O(N)
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        count = 0
        for num in nums:
            if num - k in freq:
                count += freq[num-k]
            if num + k in freq:
                count += freq[num+k]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return count
    






class Solution:
    def findPair(self, arr: list[int], x: int) -> int:
        # code here
        seen = set()
        for num in arr:
            if num - x in seen or num + x in seen:
                return True
            seen.add(num)
        return False