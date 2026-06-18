# 3614. Process String with Special Operations II

# brute approach 
# Time:  O(2^n)
# Space: O(2^n)
def processString(s:list[str],k:int) ->int:
    result = []
    for i in range(len(s)):
        if s[i].islower():
            result.append(s[i])
        elif s[i] == '*' and len(result) != 0:
            result.pop()
        elif s[i] == '#':
            result += result
        else:
            result = result[::-1]
    for i in range(len(result)):
        if i == k:
            return result[i]
    return "."


# Optimal approach 

def processStr(self, s, k):
    length = 0
    for i in range(len(s)):
        if s[i].islower():
            length += 1
        elif s[i] == '*' and length > 0:
            length -= 1
        elif s[i] == '#':
            length *= 2
    if k >= length:
        return "."
    for i in range(len(s)-1,-1,-1):
        if s[i].islower():
            length -= 1
            if k == length:
                return s[i]
        elif s[i] == '*':
            length += 1
        elif s[i] == '#':
            prev = length // 2
            k %= prev
            length = prev
        else:
            k = length - 1 - k
    return "."