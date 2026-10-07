# 32. Longest Valid Parentheses


"""
For LC 32, thinking "I need to generate/check every substring" is unnecessary because 
parentheses have a 
structural property that lets us identify valid contiguous segments during traversal.
"""





"""
Given a string containing just the characters '(' and ')', return the length of the 
longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""

# Brute Force Appraoch 
class Solution(object):
    def vpschecker(self,_s):
        stack = []
        for i in range(len(_s)):
            if _s[i] == '(':
                stack.append(_s[i])
            else:
                if len(stack) == 0:
                    return False
                e = stack.pop()
                if (_s[i] == ')' and e == '('):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
    
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                substring  = s[i:j+1]
                if self.vpschecker(substring) == True:
                    length = j - i + 1
                    maxlen = max(length,maxlen)
        return maxlen 







# Otpimal Approach using two pass counter  method 
# TC = O(2N) and SC = O(1)

"""
Left to right traversal ( forward traverse)
open , count = 0
if open == count : store result
if close > open : reset



right to left traversal ( reverse traversal)
open , close = 0
if open == count : store max result
if open > close : reset


"""
def LVPoptimal(s:str) -> int:
    # Forward pass
    open = 0
    close = 0
    ans = 0
    for char in s:
        if char == "(":
            open += 1
        else:
            close += 1
        if open == close:
            ans = max(ans,open+close)
        elif close > open:
            open = 0
            close = 0
    # Backward pass
    open = 0
    close = 0
    for i in range(len(s) -1,-1,-1):
        if s[i] == "(":
            open += 1
        else:
            close += 1
        if open == close:
            ans = max(ans,open + close)
        elif open > close:
            open = 0
            close = 0
    return ans



# Another Optimal Approach using Stack Appraoch
# TC = O(N) and SC = O(1)
def stacklvs(s):
    stack = [-1]
    maxlen = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                length = i - stack[-1]
                maxlen = max(maxlen,length)
    return maxlen