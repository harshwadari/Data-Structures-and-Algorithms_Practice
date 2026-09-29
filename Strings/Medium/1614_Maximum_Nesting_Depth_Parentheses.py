# 1614. Maximum Nesting Depth of the Parentheses


"""
Given a valid parentheses string s, return the nesting depth of s. The nesting 
depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3

 

Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.
"""




# optimal solution using stack
# TC = O(N) and SC = O(N)

def maxDepth(s):
    max_depth = 0
    current_depth = 0
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            current_depth += 1
            stack.append(s[i])
            max_depth = max(max_depth, current_depth)
        elif s[i] == ")":
            current_depth -= 1
            stack.pop()
    return max_depth


# More Optimal Approach using counter 
# TC = O(N) and SC = O(1)
def maxparenthesis(s:str) ->int:
    count = 0
    maxcount = 0
    for char in s:
        if s == '(':
            count += 1
            maxcount = max(maxcount,count)
        elif char == ')':
            count -= 1
    return maxcount 