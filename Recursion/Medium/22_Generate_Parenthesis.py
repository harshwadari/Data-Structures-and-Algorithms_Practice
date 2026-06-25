# 22. Generate Parentheses
"""
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
"""


# Optimal appraoch using recursion backtracking
# TC = O(2*N) and SC = O(2N) 
def parenthesis(n:int) -> list[str]:
    result = []
    def backtrack(open_count:int,close_count:int,arr:list[str]):
        if len(arr) == 2* n:
            result.append("".join(arr))
            return
        if open_count < n:
            arr.append('(')
            backtrack(open_count + 1,close_count,arr)
            arr.pop()
        if close_count < open_count:
            arr.append(')')
            backtrack(open_count , close_count + 1,arr)
            arr.pop()
    backtrack(0,0,[])
    return result 