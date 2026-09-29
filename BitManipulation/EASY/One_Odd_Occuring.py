# One Odd Occuring
"""
Given an array of arr[] positive integers where all numbers occur 
even number of times except one number which occurs odd number of times. Return that number.

Examples:

Input:arr[] = [1, 2, 3, 2, 3, 1, 3]
Output: 3
Explanation: 3 occurs three times.
Input:arr[] = [5, 7, 2, 7, 5, 2, 5]
Output: 5
Explanation: 5 occurs three times.
Constraints:

1 ≤ arr.size() ≤ 105+1
1 ≤ arr[i] ≤ 106
"""
# my dumbass brain solution
# TC = O(N) and SC = O(N)
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key,value in freq.items():
            if value % 2 != 0:
                return key


# Bit Magic Solution
# TC = O(N) and SC = O(1)
class Solution:
    def getOddOccurrence(self, arr):

        result = 0

        for num in arr:
            result = result ^ num

        return result