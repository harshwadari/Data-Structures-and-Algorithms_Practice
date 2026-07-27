# 47. Permutations II
"""
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


# Optimal Approach using Recursion backtracking
# TC = O(N * N!) and SC = O(N) + O(N) recusion stack space and set space
def permuatationsII(nums:list[int]) -> list[list[int]]:
    result = []
    def backtrack(index):
        if index == len(nums):
            result.append(nums[:])
            return
        unique = set()
        for i in range(index,len(nums)):
            if nums[i] in unique:
                continue
            unique.add(nums[i])
            nums[index],nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[index] , nums[i] = nums[i] , nums[index]
    backtrack(0)
    return result 