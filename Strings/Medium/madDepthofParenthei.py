# 1614. Maximum Nesting Depth of the Parentheses

# optimal solution using stack
# TC = O(N) and SC = O(N)

def maxDepth(s):
    max_depth = 0
    current_depth = 0
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            current_depth += 1
            stack.append(s[i])
            max_depth = max(max_depth, current_depth)
        elif s[i] == ")":
            current_depth -= 1
            stack.pop()
    return max_depth
print(maxDepth("(1+(2*3)+((8)/4))+1"))