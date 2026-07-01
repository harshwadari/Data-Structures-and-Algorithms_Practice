# 131. Palindrome Partitioning
"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

# Optimal appraoch using backtracking recursion
# TC = O(N *2^N) and SC = O(N)
def partition(s:list[str]) -> list[list[str]]:
    result = []
    path = []
    def isPalindrome(left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def backtrack(index):
        if index == len(s):
            result.append(path[:])
            return True
        for i in range(index,len(s)):
            if isPalindrome(index,i):
                path.append(s[index:i+1])
                backtrack(i+1)
                path.pop()
    backtrack(0)
    return result 