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
# TC = O(2N) and SC = O(26) ~ O(1)

def validAnagaram(s,t):
    if len(s) != len(t):
        return False
    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i] - ord('a'))] -= 1
    for num in freq:
        if num != 0:
            return False
    return True