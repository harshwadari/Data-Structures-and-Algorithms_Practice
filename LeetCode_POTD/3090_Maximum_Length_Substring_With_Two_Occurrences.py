# 3090. Maximum Length Substring With Two Occurrences
"""
Given a string s, return the maximum length of a substring such that it contains 
at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences 
of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences 
of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""

# Optimal Approach using Sliding Window Appraoch 
# TC = O(N) and SC = O(26) ~ O(1)
def lengthsubstring(s:str) -> int:
    maxlen = 0
    freq = {}
    left = 0
    for right in range(len(s)):
        if s[right] in freq:
            freq[s[right]] += 1
        else:
            freq[s[right]] = 1
        while freq[s[right]] > 2:
            freq[s[left]] -= 1
            left += 1
        maxlen = max(maxlen,right - left + 1)
    return maxlen 