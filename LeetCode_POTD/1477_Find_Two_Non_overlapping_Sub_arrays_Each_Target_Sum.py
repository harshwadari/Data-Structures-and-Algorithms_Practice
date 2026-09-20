# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
"""
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 1000
1 <= target <= 108
"""


# Brute Force Appraoch by generating all subarray and checking overlapping
# TC = O(N ^ 2) and SC = O(N)
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        minlen = float('inf')
        subarray = []
        for i in range(len(arr)):
            total = 0
            for j in range(i,len(arr)):
                total += arr[j]
                if total == target:
                    length = j - i + 1
                    subarray.append((i,j,length))
        for i in range(len(subarray)):
            start1,end1,len1 = subarray[i]
            for j in range(i + 1,len(subarray)):
                start2,end2,len2 = subarray[j]
                if end1 < start2 or end2 < start1:
                    minlen = min(minlen,len1 + len2)
        if minlen == float('inf'):
            return -1
        return minlen 