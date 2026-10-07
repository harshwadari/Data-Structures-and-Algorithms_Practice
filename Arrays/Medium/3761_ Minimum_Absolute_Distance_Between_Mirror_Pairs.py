# 3761. Minimum Absolute Distance Between Mirror Pairs

"""
You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

 


Example 1:

Input: nums = [12,21,45,33,54]

Output: 1

Explanation:

The mirror pairs are:

(0, 1) since reverse(nums[0]) = reverse(12) = 21 = nums[1], giving an absolute distance abs(0 - 1) = 1.
(2, 4) since reverse(nums[2]) = reverse(45) = 54 = nums[4], giving an absolute distance abs(2 - 4) = 2.
The minimum absolute distance among all pairs is 1.

Example 2:

Input: nums = [120,21]

Output: 1

Explanation:

There is only one mirror pair (0, 1) since reverse(nums[0]) = reverse(120) = 21 = nums[1].

The minimum absolute distance is 1.
"""


# brute force approach using all possibility using nested loops
# TC = O(N^2 D)  Where D is number of digits and TC = O(1)

def minMirrorPairDistance(nums):
    def reversenum(x):
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x //10
        return rev
    count = 0
    mindist = float('inf')
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            mindist = min(mindist,j - i)
    if mindist != float('inf'):
        return mindist
    else:
        return -1                
    
# optimal solution using hash map to store the reversed number and its index
# TC = O(N D)  Where D is number of digits and TC = O(N
def minMirrorPairDistance(nums):
    def reversenum(x):
        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x //10
        return rev
    count = 0
    mindist = float('inf')
    hashmap = {}
    for i in range(len(nums)):
        revnum = reversenum(nums[i])
        if revnum in hashmap:
            mindist = min(mindist, i - hashmap[revnum])
        hashmap[nums[i]] = i
    if mindist != float('inf'):
        return mindist
    else:
        return -1