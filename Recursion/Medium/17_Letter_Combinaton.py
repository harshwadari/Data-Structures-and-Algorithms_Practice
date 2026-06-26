# 17. Letter Combinations of a Phone Number
"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
"""
# TC = O(N *4^N) and SC = O(N) stack space
def letterCombinations(self, digits):
    char = {
    "2":"abc",
    "3": "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno",
    "7" : "pqrs",
    "8" : "tuv",
    "9" : "wxyz"
    }
    result = []
    def backtrack(index,subset):
        if index >= len(digits):
            result.append("".join(subset))
            return
        for ch in char[digits[index]]:
            subset.append(ch)
            backtrack(index + 1,subset)
            subset.pop()
    backtrack(0,[])
    return result