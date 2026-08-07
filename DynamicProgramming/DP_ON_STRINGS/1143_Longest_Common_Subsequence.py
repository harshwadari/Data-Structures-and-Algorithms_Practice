# 1143. Longest Common Subsequence
"""
Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


# Extremem Naive Appraoch is to generate all subsequence of two given strings and find common one 
# TC = 2 ^ n+M


# Recursive approach 
# TC = O(2 ^n + 2 ^m) and SC = O(max(N , M) stack space
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        def backtrack(index1,index2):
            if index1 < 0 or index2 < 0:
                return 0
            if text1[index1] == text2[index2]:
                return 1 + backtrack(index1 - 1,index2 -1)
            return 0 + max(backtrack(index1-1,index2),backtrack(index1,index2 - 1))
        return backtrack(len(text1) - 1,len(text2) - 1)




# Memoization Appraoch 
# TC = O(N * M) and SC = O(N * M) dp space O(N + M) stack space
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def backtrack(index1,index2):
            if index1 < 0 or index2 < 0:
                return 0
            if dp[index1][index2] != -1:
                return dp[index1][index2]
            if text1[index1] == text2[index2]:
                dp[index1][index2] =  1 + backtrack(index1 - 1,index2 -1)
                return dp[index1][index2]
            dp[index1][index2]  = 0 + max(backtrack(index1-1,index2),backtrack(index1,index2 - 1))
            return dp[index1][index2]
        return backtrack(len(text1) - 1,len(text2) - 1)



# Tabulation Appraoch 
# TC = O( N * M)  and SC = O(N * M)
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        for index2 in range(m+1):
            dp[0][index2] = 0
        for index1 in range(n + 1):
            dp[index1][0] = 0
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if text1[i-1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]


# Tabulation with Space Optimization 
# TC = O(N * M ) and SC = O(2M) variable sapce 
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        prev= [0 for _ in range(m + 1)]
        for index2 in range(m+1):
            prev[index2] = 0
        for i in range(1,n + 1):
            curr = [0 for _ in range(m + 1)]
            for j in range(1,m + 1):
                if text1[i-1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = 0 + max(prev[j],curr[j-1])
            prev = curr
        return prev[m]


