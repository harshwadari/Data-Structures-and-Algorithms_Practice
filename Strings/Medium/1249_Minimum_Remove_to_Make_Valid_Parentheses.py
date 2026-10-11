# 1249. Minimum Remove to Make Valid Parentheses
"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""

# stack Appraoch 
# TC = O(3N)  two for loops and one while loop and SC = one set and one result arr and one set O(3N)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        myset = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack)!= 0:
                    stack.pop()
                else:
                    myset.add(i)
        while len(stack)!= 0:
            myset.add(stack.pop())
        result = []
        for i in range(len(s)):
            if i not in myset:
                result.append(s[i])
        return "".join(result)



# another two pass appraoch
# TC = O(2N) and SC = O(2N)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # first pass from left to right 
        open = 0
        result = []
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                result.append(s[i])
            elif s[i] == "(":
                open += 1
                result.append(s[i])
            elif s[i] == ")":
                if open > 0:
                    open -= 1
                    result.append(s[i])
        result = result[::-1]
        close = 0
        final = []
        for i in range(len(result)):
            if 'a' <= result[i] <= 'z':
                final.append(result[i])
            elif result[i] == ')':
                close += 1
                final.append(result[i])
            elif result[i] == "(":
                if close > 0:
                    close -= 1
                    final.append(result[i])
        return "".join(final[::-1])