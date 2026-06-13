# Prefix to Infix expression conversion
# TC = O(N) and SC = O(N)
def preToInfix(self, s):
        # Code here
        stack = []
        for char in s[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_expression = f'({operand1}{char}{operand2})'
                stack.append(new_expression)
        return stack[0]