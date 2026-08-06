# 525. Contiguous Array
"""
Given a binary array nums, return the maximum length of a contiguous subarray with an 
equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 10 ^ 5
nums[i] is either 0 or 1.
"""
# Brute Force Appraoch 
# TC = O(N ^ 3) and SC = O(1)
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                zero = 0
                one = 0
                for k in range(i,j+1):
                    if nums[k] == 0:
                        zero += 1
                    else:
                        one += 1
                if zero == one:
                    length = j - i + 1
                    maxlen = max(length,maxlen)
        return maxlen 



# Better Appraoch
# TC = O(N ^ 2) and SC  = O(1)
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        for i in range(len(nums)):
            one = 0
            zero = 0
            for j in range(i+1,len(nums)):
                if nums[j] == 1:
                    one += 1
                else:
                    zero += 1
                if zero == one:
                    length = j - i + 1
                    maxlen = max(length,maxlen)
        return maxlen 



# Optimal Appraoch using prefix sums
# TC = O(N) and SC = O(N)
def array(nums):
    prefix = {0:-1}
    current_sum = 0
    maxlen = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            current_sum += 1
        else:
            current_sum -= 1
        if current_sum in prefix:
            length = i - prefix[current_sum]
            maxlen = max(maxlen,length)
        else:
            prefix[current_sum] = i
    return maxlen       