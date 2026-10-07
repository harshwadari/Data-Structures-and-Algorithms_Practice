# 678. Valid Parenthesis String
"""
Given a string s containing only three types of characters: '(', ')' and '*', 
return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis
 '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
Example 4:

Input: s = "("
Output: false
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""


# Recursion Backtracking Appraoch
# TC = O(3^N) and SC = O(N)
class Solution(object):
    def checkValidString(self, s):
        def backtrack(i,count):
            if count < 0:
                return False
            if i == len(s):
                return count == 0
            if s[i] == "(":
                return backtrack(i+1,count+1)
            elif s[i] == ")":
                return backtrack(i+1,count-1)
            else:
                return (backtrack(i+1,count+1) or
                backtrack(i+1,count-1)or
                backtrack(i+1,count))
        return backtrack(0,0)


# Memoization Appraoch 
# TC = O(N ^ 2) and SC = O(N^ 2 + N) stack space 
class Solution(object):
    def checkValidString(self, s):

        n = len(s)

        # dp[index][balance]
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(index, balance):

            if balance < 0:
                return False

            if index == n:
                return balance == 0

            if dp[index][balance] != -1:
                return dp[index][balance]

            if s[index] == "(":
                result = solve(index + 1, balance + 1)

            elif s[index] == ")":
                result = solve(index + 1, balance - 1)

            else:
                result = (
                    solve(index + 1, balance + 1) or
                    solve(index + 1, balance - 1) or
                    solve(index + 1, balance)
                )

            dp[index][balance] = result
            return result

        return solve(0, 0)

    






# Counter appraoch
# TC = O(2N) and SC = O(1)
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # left to right traverse
        open = 0
        close = 0
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                open += 1
            else:
                open -= 1
            if open < 0:
                return False

        # right to left traverse
        open = 0
        close = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ")" or s[i] == "*":
                close += 1
            else:
                close -= 1
            if close < 0:
                return False
        return True