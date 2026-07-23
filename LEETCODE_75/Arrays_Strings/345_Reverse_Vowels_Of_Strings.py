# 345. Reverse Vowels of a String
"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower 
and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

# Better approach using hard work
# TC = O(N) and SC= O(N)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)):
            if s[i]=='A'or s[i]=='a'or s[i]=='E'or s[i]=='e'or s[i]=='I'or s[i]=='i'or s[i]=='O'or s[i]=='o'or s[i]=='U'or s[i]=='u':
                result.append(s[i])
        result.reverse()
        idx = 0
        s = list(s)
        for i in range(len(s)):
            if s[i]=='A'or s[i]=='a'or s[i]=='E'or s[i]=='e'or s[i]=='I'or s[i]=='i'or s[i]=='O'or s[i]=='o'or s[i]=='U'or s[i]=='u':
                s[i] = result[idx]
                idx += 1
        return "".join(s)

# Optimal Appraoch using hashset and two pointer
# TC = O(N) and SC = O(1)
def vowelReverse(s:list[str]):
    vowel = {'a','e','i','o','u','A','E','I','O','U'}
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and s[left] not in vowel:
            left += 1
        while left < right and s[right] not in vowel:
            right -= 1
        s[left] ,s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)
