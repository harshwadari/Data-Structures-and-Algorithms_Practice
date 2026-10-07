# 921. Minimum Add to Make Parentheses Valid
"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a 
parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to
 be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""

# Otpimal Appraoch using stack 
# TC = O(N) and SC = O(N)
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")" and len(stack) != 0:
                stack.pop()
            else:
                count += 1
        return len(stack) + count






    
# another appraoch without stack 
# TC = O(N) and SC = O(1)
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = 0
        count = 0
        for char in s:
            if char == "(":
                size += 1
            elif char == ")" and stack  != 0:
                stack -= 1
            else:
                count += 1
        return stack + count