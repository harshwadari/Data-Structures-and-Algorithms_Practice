# Prefix to Postfix conversion
# TC = O(2N) and SC = O(N)

def preToPost( s):
    # Code here
    stack = []
    for char in s[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expression = f'{operand1}{operand2}{char}'
            stack.append(new_expression)
    return stack[0]