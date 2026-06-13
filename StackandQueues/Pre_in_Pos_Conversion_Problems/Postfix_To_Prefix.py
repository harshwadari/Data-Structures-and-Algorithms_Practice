# Postfix to prefix conversion

def postfixTOprefix(s):
    stack = []
    for char in s:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expression = f'{char}{operand1}{operand2}'
            stack.append(new_expression)
    return stack[0]