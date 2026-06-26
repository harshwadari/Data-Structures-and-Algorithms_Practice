# 216. Combination Sum III
"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""

def combinationSum3(k:int, n:int)-> list[list[int]]:
    result = []
    def backtrack(index,total,subset):
        if len(subset) == k:
            if total == n:
                result.append(subset[:])
            return
        if total > n:
            return
        for i in range(index,10):
            subset.append(i)
            backtrack(i + 1,total + i,subset)
            subset.pop()
    backtrack(1,0,[])
    return result