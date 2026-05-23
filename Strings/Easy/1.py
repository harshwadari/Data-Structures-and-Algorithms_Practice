# 1021. Remove Outermost Parentheses

"""
Docstring for Strings.Easy.1

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""


# optimal approach
# TC = O(N) and SC = O(N) and maybe sc is O(1) coz string extra space doesn't count

def outermost(s):
    n = len(s)
    count = 0
    result = ""
    for i in range(n):
        if s[i] == "(":
            count +=1
            if count >1:
                result += s[i]
        else:
            count -=1
            if count >0:
                result += s[i]
    return result
print(outermost("(())"))
    