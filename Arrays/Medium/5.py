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


# better approach
# TC = O(nlogN + N) and SC = O(1)
def longest(nums):
    nums.sort()
    last_small = float('-inf')
    count = 0
    longest = 0
    for i in range(len(nums)):
        num = nums[i]
        if num - 1 == last_small:
            count +=1
            last_small = num
        elif num != last_small:
            count = 1
            last_small = num
        longest = max(longest , count)
    return longest

