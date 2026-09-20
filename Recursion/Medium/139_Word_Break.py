# 139. Word Break
"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


# Backtracking Approach 
# TC = O( 2 * n * n) and SC = O(N) stack Space and O(N) Auxilary Space
def wordBrak(s:str,wordDict:list[str]):
    wordSet = set(wordDict)
    def backtrack(index):
        if index == len(s):
            return True
        for j in range(index + 1,len(s) +1):
            word = s[index:j]
            if word in wordSet:
                if backtrack(j):
                    return True
        return False
    return backtrack(0)