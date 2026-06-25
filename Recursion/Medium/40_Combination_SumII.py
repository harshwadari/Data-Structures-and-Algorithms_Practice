# 40. Combination Sum II
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
"""
the brute-force approach is:

Generate all subsequences.
If the sum equals target, sort the subsequence.
Store it in a set to remove duplicates.
Convert the set back to a list.
"""
# TC = O(2^N * KlogK) and SC = O(N) + O(K)
def combinationSum2(self, candidates, target):
    
    result = set()
    def backtrack(index, total, subset):
        if index == len(candidates):
            if total == target:
                temp = sorted(subset)
                result.add(tuple(temp))
            return
        # Pick
        subset.append(candidates[index])
        backtrack(index + 1, total + candidates[index], subset)
        subset.pop()
        # Not Pick
        backtrack(index + 1, total, subset)
    backtrack(0, 0, [])
    ans = []
    for comb in result:
        ans.append(list(comb))
    return ans