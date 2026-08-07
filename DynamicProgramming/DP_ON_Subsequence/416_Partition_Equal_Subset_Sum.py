# 416. Partition Equal Subset Sum
"""
Given an integer array nums, return true if you can partition 
\the array into two subsets such that the sum of the elements in both subsets 
is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

# Recursive Approach using Backtracking
# TC = O(N ^ 2) and SC = O(N)
def paritionSubset(nums:list[int]) -> bool:
    k = sum(nums)
    if k % 2 == 1:
        return False
    target = k // 2
    def backtrack(index,total):
        if total == 0:
            return True
        if index == 0:
            if nums[0] == total:
                return True
            return False
        if nums[index] > total:
            pick = False
        else:
            pick = backtrack(index - 1,total - nums[index])
        notpick = backtrack(index - 1,total)
        if pick == True or notpick == True:
            return True
        else:
            return False
    return backtrack(len(nums) - 1,target)



# Memoization Appraoch 
# TC = O(N * Target) and SC = O(N) stack space and O(N * Target ) dp space
def MemoPartionSubset(nums:list[int]) -> bool:
    k = sum(nums)
    n  = len(nums)
    if k % 2 == 1:
        return False
    target = k // 2
    dp = [[-1] * ( target + 1) for _ in range(n)]
    def backtrack(index,total):
        if total == 0:
            return True
        if index == 0:
            if nums[0] == total:
                return True
            return False
        if dp[index][total] != -1:
            return dp[index][total]
        if nums[index] > total:
            pick = False
        else:
            pick = backtrack(index - 1,total - nums[index])
        notpick = backtrack(index - 1,total)
        dp[index][total] = pick or notpick
        return dp[index][total]
    return backtrack(len(nums) - 1,target)



# Tabulation Appraoch 
# TC = O(N * target) and SC = O(n * target)

def Tabupartition(nums:list[int]) -> bool:
    n = len(nums)
    k = sum(nums)
    if k % 2 == 1:
        return False
    target = k // 2
    dp = [[-1] * (target + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    if nums[0] <= target:
        dp[0][nums[0]] = True
    for index in range(1,n):
        for total in range(1,target + 1):
            if nums[index] > total:
                pick = False
            else:
                pick = dp[index -1][total - nums[index]]
            notpick = dp[index - 1][total]
            dp[index][total] = pick or notpick
    return dp[n - 1][target]



# Tabulation with Sapce Optimaization
# TC = O(N * Target ) and SC = O(Target)
def SpacePartition(nums:list[int]) -> bool:
    k = sum(nums)
    if k % 2 == 1:
        return False
    target = k // 2
    