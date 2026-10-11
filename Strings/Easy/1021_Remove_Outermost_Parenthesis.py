# 1021. Remove Outermost Parentheses

"""
Docstring for Strings.Easy.1

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".



Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
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





# More optimal appraoch because in python strings are immutable += creates new string at every iteration making compleixity high
# TC = O(N) and SC = O(1) Auxilary Space
def Outermostoptimal(s:str) -> str:
    ans = []
    count = 0
    for char in s:
        if char == "(":
            count += 1
            if count > 1:
                ans.append("(")
        else:
            count -= 1
            if count > 0:
                ans.append(")")
    return "".join(ans)