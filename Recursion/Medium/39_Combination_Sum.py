# 39. Combination Sum
"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

# TC = O(2^t *K) and SC = O(N) + O(K) where N is stack Space 
def combinationSum(candidates, target):
    result = []
    def backtrack(index,total,subset):
        if index == len(candidates):
            return
        if total == target:
            result.append(subset[:])
            return
        if total > target:
            return
        subset.append(candidates[index])
        backtrack(index,total + candidates[index],subset)
        subset.pop()
        backtrack(index + 1,total,subset)
    backtrack(0,0,[])
    return result