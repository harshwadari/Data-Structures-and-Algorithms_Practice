# 128. Longest Consecutive Sequence
"""
Docstring for Arrays.Medium.5

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 
"""


# brute force 
# TC = O(N^2) and SC = O(1)

def longestconsecutive(nums):
    n = len(nums)
    max_count = 0
    for i in range(n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count +=1
            num = num +1
        max_count = max(max_count,count)
    return max_count


# better approach using Sorting 
# TC = O(NlogN + N) and SC = O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        maxlen = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                length += 1
                maxlen = max(maxlen, length)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                length = 1
        return maxlen


#Optimal Appraoch using HashSet
# TC = O(N) and SC = O(N)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        myset = set(nums)
        maxlen = 1
        for num in myset: 
            if num - 1 not in myset:
                length = 1
                curr= num
                while curr + 1 in myset:
                    length += 1
                    curr += 1
                maxlen = max(maxlen,length)
        return maxlen
