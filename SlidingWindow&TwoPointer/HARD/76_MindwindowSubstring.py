# Minimum window substring 


# brute code 
"""
First generate all substring and then check for each substring it contains same as another string
"""
# TC = O(N^3) and SC = O(256)
def minwindsubstring(s,t):
    def isvalid(sub,t):
        freq = {}
        for char in sub:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1
        for char in t :
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -=1
        return True
    n = len(s)
    minlen = float('inf')
    result = ""
    for i in range(n):
        for j in range(i,n):
            sub = s[i: j+1]
            if isvalid(sub,t):
                if len(sub) < minlen:
                    minlen = len(sub)
                    result = sub
    return result