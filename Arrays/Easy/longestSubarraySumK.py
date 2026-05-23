# Longest subarray with sum k 

"""
Docstring for Arrays.Easy.9
Given an array nums of size n and an integer k, find the length o
f the longest sub-array that sums to k. If no such sub-array 
exists, return 0.
"""

# brute force method by generating all existing subarrays and checking 
#Tc = O(N^2) and SC = O(1)

def longestSubarry(nums,k):
    n = len(nums)
    length = 0
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            if sum == k:
                length = max(length , j-i+1)
    return length
print(longestSubarry([10,5,2,7,1,9],15))


# optimal  appraoch using prefix sum and hasing 
# TC = O(N) and SC = O(1)
def longsub(nums,k):
    n =len(nums)
    prefixmap= {}
    prefixsum = 0
    maxlen = 0
    for i in range(n):
        prefixsum += nums[i]
        if prefixsum == k:
            maxlen = i + 1
        if (prefixsum - k) in prefixmap:
            length = i - prefixmap[prefixsum - k]
            maxlen = max(maxlen, length)
        if prefixsum not in prefixmap:
            prefixmap[prefixsum ] = i
    return maxlen 


# more optimal approach using sliding window if array has only positive elements
# TC = O(N) and SC = O(1)
def subarray(arr,k):
    left = 0
    sum = 0
    maxlen = 0
    for right in range(len(arr)):
        sum += arr[right]
        while sum > k:
            sum -= arr[left]
            left +=1
        if sum == k:
            maxlen = max(maxlen, right - left + 1)
    return maxlen 