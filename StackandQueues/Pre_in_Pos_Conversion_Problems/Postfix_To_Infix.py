# Postfix to Infix expression conversion
# TC = O(N) and SC = O(N)
def postfixTOinfix(s):
    stack = []
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expression = f'({operand1}{char}{operand2})'
            stack.append(new_expression)
    return stack[0]