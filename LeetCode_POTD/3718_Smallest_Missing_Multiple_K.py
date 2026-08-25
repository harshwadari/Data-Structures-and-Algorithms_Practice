# 3718. Smallest Missing Multiple of K
"""
Given an integer array nums and an integer k, return the smallest positive multiple of 
k that is missing from nums.

A multiple of k is any positive integer divisible by k.

 

Example 1:

Input: nums = [8,2,3,4,6], k = 2

Output: 10

Explanation:

The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple 
missing from nums is 10.

Example 2:

Input: nums = [1,4,7,10,15], k = 5

Output: 5

Explanation:

The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 100
"""


# My Brute Appraoch 
# TC = O(2N) and SC = O(2N)
def mineMissingMultiple(nums:list[int],k:int):
    lookup = set(nums)
    result = []
    for i in range(1,len(nums)+2):
        result.append(i * k)
    for num in result:
        if num not in lookup:
            return num


# Most Optimal Approach 
# TC = O(N) and SC = O(N)
def optimalMissingMultiple(nums:list[int],k:int):
    lookup = set(nums)
    for i in range(1,len(nums)+2):
        multiple = i * k
        if multiple not in lookup:
            return multiple



# Sorting Appraoch 
# TC = O(Nlogn) and SC = O(1)
def sortingMissingMultiple(nums:list[int],k:int):
    pass 
