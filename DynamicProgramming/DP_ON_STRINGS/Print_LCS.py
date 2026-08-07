# Print Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
        n, m = len(text1), len(text2)

        # 1) Build DP table (lengths)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 2) Backtrack from bottom-right to build one LCS
        i, j = n, m
        lcs_chars = []
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                lcs_chars.append(text1[i - 1])  # pick the char
                i -= 1
                j -= 1
            else:
                # Move in the direction of the larger value
                if dp[i - 1][j] >= dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        # 3) Reverse and join to get the LCS string
        return ''.join(reversed(lcs_chars))