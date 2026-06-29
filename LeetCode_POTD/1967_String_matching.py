# 1967. Number of Strings That Appear as Substrings in Word
"""
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
"""

# Optimal approach uisng py built in (in) function
# TC = O(N * M * K) where n = len(patterns) m = len(word) k = average length of a pattern and SC = O(1)

def substring(s:list[str],word:int) -> int:
    count = 0
    for char in s:
        if char in word:
            count += 1
    return count


# Manual appraoch without using built in function
# TC and SC will be same 

def numOfStrings(self, patterns, word):
    count = 0
    for pattern in patterns:
        found = False
        for i in range(len(word) - len(pattern) + 1):
            match = True
            for j in range(len(pattern)):
                if word[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                found = True
                break
        if found:
            count += 1
    return count