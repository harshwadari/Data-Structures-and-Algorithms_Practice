# 60. Permutation Sequence
"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following 
sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
"""



# Recursive Backtracking Appraoch
# TC = O(N ! * N) and SC = O(N)
class Solution(object):
    def getPermutation(self, n, k):

        nums = []

        for i in range(1, n + 1):
            nums.append(i)

        result = []

        def backtrack(index):

            if index == len(nums):
                result.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]

                backtrack(index + 1)

                nums[index], nums[i] = nums[i], nums[index]

        backtrack(0)

        return "".join(map(str, result[k - 1]))



# Otpimal Appraoch using factorial math
# TC = O(N ^2) and SC = O(N)
class Solution(object):
    def getPermutation(self, n, k):
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        result = ""
        k = k - 1
        for i in range(n):
            fact = 1
            for j in range(1,n - i):
                fact *= j
            index = k // fact
            result += str(nums[index])
            nums.pop(index)
            k = k % fact
        return result
