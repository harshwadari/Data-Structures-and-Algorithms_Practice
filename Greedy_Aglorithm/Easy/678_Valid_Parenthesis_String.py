# Valid Parenthesis lc 
# TC = O(N) and SC = O(1)
# optimal solution using two pointer

def validstring(s):
    min = 0
    max = 0
    for i in range(len(s)):
        if s[i] == "(":
            min += 1
            max += 1
        elif s[i] == ')':
            min -=1 
            max += 1
        else:
            min -= 1
            max += 1
        if min < 0:
            min = 0
        if max < 0:
            return False
    if min == 0:
        return True
    return False