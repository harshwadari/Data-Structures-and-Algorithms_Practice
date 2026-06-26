# 90. Subsets II

"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


# Optimal appraoch using recursion backtracking
# TC = O(N * 2^N) and SC = O(n × 2ⁿ) (required to store all subsets)
def subsetsWithDup(self, nums):
    nums.sort()
    result = []
    def backtrack(index,subset):
        result.append(subset[:])
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
    backtrack(0,[])
    return result 