"""
Steps to convert infix to prefix
-----------------------------------
1. Reverse the given infix expression
2. Replace '(' with ')' and vice versa
3. Apply full infix to postfix logic 
3. rerverse again the final answer 
"""
# TC = O(6N) and SC = O(2N)
def presedence(ch):
    if ch == '+' or ch == '-':
        return 1
    if ch == '*' or ch == '/':
        return 2
    if ch == '^':
        return 3
    return 0
def infixTOprefix(s:str) -> str:
    s = s[::-1]
    s = s.replace('(' ,'temp').repalce(')','(').replace('temp',')')
    stack = []
    result = []
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= 9):
            result.append(char)
        elif char == '(':
            result.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and presedence(stack[-1]) > presedence(char):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return "".join(result[::-1])