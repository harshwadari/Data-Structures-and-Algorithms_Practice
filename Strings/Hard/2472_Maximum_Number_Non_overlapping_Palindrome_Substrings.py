# 2472. Maximum Number of Non-overlapping Palindrome Substrings
"""
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.
"""

# Brute Force Appraoch 
"""
Brute Force
────────────────
Generate substrings     O(n²)
Check palindrome        O(n³)  ← dominant
Sort                    O(n² log n)
Greedy selection        O(n²)

TOTAL                   O(n³)
SPACE                   O(n²)
"""

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        palindrome = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                if j - i + 1 >= k:
                    substring = s[i:j+1]
                    if substring == substring[::-1]:
                        palindrome.append([i,j])
        palindrome.sort(key=lambda x: x[1])
        count = 0
        end = -1
        for start , finish in palindrome:
            if start > end:
                count += 1
                end = finish
        return count


# better Appraoch using 2DP for stroing and checking valid palindromic substring
"""
2D DP

────────────────

Create dp table          O(n²)

Build palindrome table   O(n²)

Create best array        O(n)

Calculate best DP        O(n²)  ← dominant

TOTAL                    O(n²)

SPACE                    O(n²)
"""

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # create 2dp table by initalizing with all False
        dp = [[False] * n for _ in range(n)]
        # Every single char is palindrome itself 
        for i in range(n):
            dp[i][i] = True
        for length in range(2,n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        ans = [0] * n
        for i in range(n):
            if i > 0:
                ans[i] = ans[i-1]
            for j in range(i+1):
                length = i - j + 1
                if length >= k and dp[j][i]:
                    if j == 0:
                        ans[i] = max(ans[i],1)
                    else:
                        ans[i] = max(ans[i],ans[j-1] + 1)
        return ans[n-1]




# Most Optimal Appraoch using Manacher's Algorithm
