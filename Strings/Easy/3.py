# 242. Valid Anagram


"""
Docstring for Strings.Easy.3

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"

Output: false
"""



# brute approach using sorting 
# TC = O(2NlogN) and SC = O(2N)
def anagram(s,t):
    if len(s) != len(t):
        return False
    sort_s = sorted(s)
    sort_t = sorted(t)
    if sort_s == sort_t:
        return True
    return False
print(anagram("cat","atc"))



# optimal approach using dictionary
# TC = O(3N) and SC = O(N)/

def validAnagaram(s,t):
    if len(s) != len(t):
        return False
    map = {}
    for i in range(len(s)):
        char = s[i]
        if char in map:
            map[char] +=1
        else:
            map[char] =1
    for i in range(len(t)):
        char = t[i]
        if char not in map:
            return False
        else:
            map[char]-=1
    for char in map:
        if map[char] !=0:
            return False
    return True