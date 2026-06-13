"""
Operator : Symbol that performs an operation (+, -, *, /)

Operand : Values on which operators act (2 and 3 in 2+3)

Infix   : Operator is between operands (A + B)

Prefix  : Operator comes before operands (+ A B)

Postfix : Operator comes after operands (A B +)
"""


# Infix to postfix conversion
# TC = O(2N) and SC = O(N)
class Solution:
    def presedence(self,ch):
        if ch == '+' or ch == "-":
            return 1
        if ch == '*' or ch == '/':
            return 2
        if ch == "^":
            return 3
        return 0
    def infixtoPostfix(self, s):
        #code here
        stack = []
        result = []
        for char in s:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != '(' and (self.presedence(stack[-1]) > self.presedence(char) or (self.presedence(stack[-1]) == self.presedence(char) and char != '^'))):
                    result.append(stack.pop())
                stack.append(char)
        while stack :
            result.append(stack.pop())
        return "".join(result)
