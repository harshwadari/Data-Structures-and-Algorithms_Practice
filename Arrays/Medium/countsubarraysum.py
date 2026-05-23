# 560. Subarray Sum Equals K

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""


# brut force approach by finding all subbaray using nested for loops
# TC = O(N^2) and SC = O(1)

def subarraysum(nums,k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum == k:
                count +=1
    return count



# optimal approach using prefix sum and hashing
# TC = O(N) and SC = O(N)
def countsubarraySum(nums,k):
    prefixsum = 0
    prefixmap = {0 : 1}
    count = 0
    for i in range(len(nums)):
        prefixsum += nums[i]
        if (prefixsum - k) in prefixmap:
            count += prefixmap[prefixsum - k]
        if prefixsum in prefixmap:
            prefixmap[prefixsum] +=1
        else:
            prefixmap[prefixsum] = 1 
    return count 