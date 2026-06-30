# 1358. Number of Substrings Containing All Three Characters

"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
"""

# Brute force appraoch by generating all substring anc checking
# TC = O(N^2) and SC = O(1)
def substring(s:list[str]):
    count = 0
    for i in range(len(s)):
        freq = {}
        for j in range(i,len(s)):
            if s[j] in freq:
                freq[s[j]] += 1
            else:
                freq[s[j]] = 1
            if 'a' in freq and 'b' in freq and 'c' in freq:
                count += 1
    return count


# Otpimal approach 
# TC = O(N) and SC = O(1)
def optimalsubstrin(s:list[str]):
    last_seen = [-1,-1,-1]
    count = 0
    for i in range(len(s)):
        last_seen[ord(s[i]) - ord('a')] = i
        if min(last_seen) != -1:
            count += min(last_seen) + 1
    return count
