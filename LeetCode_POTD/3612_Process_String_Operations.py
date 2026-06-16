# 3612. Process String with Special Operations I

"""You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the final string result after processing all characters in s.
"""

# Optimal solution using stack operations

# TC = O(2^N) and SC = O(2^N)
def processStr(self, s):
    stack = []
    for i in range(len(s)):
        if ('a' <= s[i] <= 'z'):
            stack.append(s[i])
        elif s[i] == '*' and len(stack) != 0:
            stack.pop()
        elif s[i] == '#':
            stack += stack
        else:
            stack = stack[::-1]
    return "".join(stack)