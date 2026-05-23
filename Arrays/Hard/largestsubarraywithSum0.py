# largest subarray with sum equals to zero

"""
Given an array arr[] containing both positive and negative integers, the task is to find the length of the longest subarray with a sum equals to 0.

Note: A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

Examples:

Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].
"""


# brute force appraoch using nested for loops
# Tc = O(N^2) and SC = O(1)

def subarraysum0(nums):
    length = 0
    maxLength = 0
    for i in range(len(nums)):
        currsum = 0
        for j in range(i, len(nums)):
            currsum += nums[j]
            if currsum == 0:
                length = j - i +1
                maxLength = max(maxLength,length)
    return maxLength
print(subarraysum0([15, -2, 2, -8, 1, 7, 10, 23]))




# optimal approach using prefix sum and hashmap
# Tc = O(N) and SC = O(N)


def maxLength(self, arr):
        # code here
        n = len(arr)
        maxlength = 0
        currsum = 0
        length = 0
        map = {}
        for i in range(n):
            currsum += arr[i]
            if currsum == 0:
                maxlength = i+1
            if currsum in map:
                length = i - map[currsum]
                maxlength = max(maxlength,length)
            else:
                map[currsum] = i
        return maxlength