# Longest Substring without Repeating Characters

# brute force approach using nested loops
# TC = O(N ^ 2) and SC = O(256)
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    longest = 0
    for i in range(n):
        map = [0] * 256
        for j in range(i, n):
            if map[ord(s[j])] == 1:
                break
            else:
                map[ord(s[j])] = 1  
            longest = max(longest, j - i + 1)
    return longest
print(lengthOfLongestSubstring('abcabcbb'))



# Optimal approach using sliding windows and hashing 
"""
💡 Idea:
Use two pointers: left and right
Expand right to include characters
If duplicate found → move left forward
Always maintain substring with unique chars
"""
# TC = O(N) and SC = O(k) where k is number of unique chars

# using set 
def lenthtofLongestsubstring(s):
    n = len(s)
    left = 0
    maxlen = 0
    chars = set()
    for right in range(n):
        while s[right] in chars:
            chars.remove(s[left])
            left +=1
        chars.add(s[right])
        maxlen = max(maxlen, right - left + 1)
    return maxlen


# using hashmap
def longsubstring(s):
    n = len(s)
    maxlen = 0
    lastSeen = {}
    left = 0
    for right in range(n):
        if s[left] in lastSeen:
            left = max(left , lastSeen[s[right]] + 1)
        lastSeen[s[right]] = right
        maxlen = max(maxlen, right - left + 1)
    return maxlen