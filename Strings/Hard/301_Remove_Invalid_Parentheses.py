# 301. Remove Invalid Parentheses
"""
Given a string s that contains parentheses and letters, remove the minimum 
number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of 
removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        maxlen = [0]
        def backtrack(index,curr,count):
            # nonlocal maxlen
            if count < 0:
                return
            if index == len(s):
                if count == 0:
                    if len(curr) > maxlen[0]:
                        maxlen[0] = len(curr)
                        result.clear()
                    if len(curr) == maxlen[0]:
                        result.add("".join(curr))
                return
            if s[index] != "("  and s[index] != ")":
                curr.append(s[index])
                backtrack(index+1,curr,count)
                curr.pop()
                return
            curr.append(s[index])
            if s[index] == "(":
                backtrack(index + 1,curr,count+1)
            else:
                backtrack(index + 1,curr,count -1)
            curr.pop()
            backtrack(index + 1,curr,count)
        backtrack(0,[],0)
        return list(result)
















class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res = []
        stack = [(s, 0, 0, ("(", ")"))]

        while stack:
            cur, li, lj, par = stack.pop()
            n = len(cur)
            bal = 0
            match = False

            for i in range(li, n):
                bal += (cur[i] == par[0]) - (cur[i] == par[1])
                if bal >= 0:
                    continue

                for j in range(lj, i + 1):
                    if cur[j] == par[1] and (j == lj or cur[j - 1] != par[1]):
                        nxt = cur[:j] + cur[j + 1 :]
                        stack.append((nxt, i, j, par))

                match = True
                break

            if not match:
                rev = cur[::-1]

                if par[0] == "(":
                    stack.append((rev, 0, 0, (")", "(")))
                else:
                    res.append(rev)

        return res