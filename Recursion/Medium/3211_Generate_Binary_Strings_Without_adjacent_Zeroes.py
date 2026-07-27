# 3211. Generate Binary Strings Without Adjacent Zeros
"""
You are given a positive integer n.

A binary string x is valid if all substrings of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

 

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".

 

Constraints:

1 <= n <= 18

"""

# Optimal Approach using recursion backtracking
# TC = O(2^N) and SC = O(N) stack space
class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(index, string):
            if index == n:
                ans.append("".join(string))
                return
            # Always place 0
            string.append('1')
            backtrack(index + 1, string)
            string.pop()
            # Place 1 only if previous is not 1
            if len(string) == 0 or string[-1] != '0':
                string.append('0')
                backtrack(index + 1, string)
                string.pop()
        backtrack(0, [])
        return ans