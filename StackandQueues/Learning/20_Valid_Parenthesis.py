# 20. Valid Parentheses

# TC = O(N) and SC = O(N)
def isValid(self, s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            e = stack.pop()
            if (s[i] == ')' and e == '(') or (s[i] == ']' and e == '[' or (s[i] == '}' and e == '{')):
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    return False
    