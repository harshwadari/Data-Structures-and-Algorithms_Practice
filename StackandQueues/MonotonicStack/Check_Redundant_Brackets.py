# Check Redundant Brackets
"""
Given a string of balanced expression s, check if it contains a redundant parenthesis or not. A set of parenthesis are redundant if the same sub-expression is surrounded by unnecessary or multiple brackets.
Note: Expression may contain + , - , *, and / operators. Given expression is valid and there are no white spaces present.

Examples:

Input: s = "((a+b))"
Output: true 
Explanation: ((a+b)) can reduced to (a+b).
Input: s = "(a+(b)/c)"
Output: true
Explanation: (a+(b)/c) can reduced to (a+b/c) because b is surrounded by () which is redundant.
Input: s = "(a+b+(c+d))"
Output: false
Explanation:(a+b+(c+d)) doesn't have any redundant or multiple brackets.
Constraints:
1 ≤ |s| ≤105
"""


class Solution():
    def checkRedundancy(self, s):
        # code here 
        stack = []
        for char in s:
            if char == ")":
                ops = False
                while len(stack) !=  0 and stack[-1] != "(":
                    top = stack.pop()
                    if top in "+-*/":
                        ops = True
                stack.pop()
                if ops == False:
                    return True
            else:
                stack.append(char)
        return False