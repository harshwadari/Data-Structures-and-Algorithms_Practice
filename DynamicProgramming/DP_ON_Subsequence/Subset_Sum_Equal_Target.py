# Subset Sum Problem
"""
Given an array of positive integers arr[] and a value sum, determine 
if there is a subset of arr[] with sum equal to given sum. 

Examples:

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: true 
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: false
Explanation: There is no subset with target sum 30.
Input: arr[] = [1, 2, 3], sum = 6
Output: true
Explanation: The entire array can be taken as a subset, giving 1 + 2 + 3 = 6.
Constraints:
1 <= arr.size() <= 200
1<= arr[i] <= 200
1<= sum <= 104
"""

# Recursive Approach
# TC = O(2^N) and SC = O(N) stack space
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        def backtrack(idx,total):
            if total == 0:
                return True
            if idx == 0:
                if arr[0] == total:
                    return True
                return False
            if arr[idx] > total:
                pick =  False
            else:
                pick = backtrack(idx - 1,total-arr[idx])
            notpick = backtrack(idx-1,total)
            if pick == True or notpick == True:
                return True
            else:
                return False
        return backtrack(len(arr) - 1,sum)


# Memoization Approach 
# TC = O(N * sum) and SC = O(N) dp array  + O(N) stack space

class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n = len(arr)
        dp = [[-1 for _ in range(sum+1)] for _ in range(n)]
        # code here
        def backtrack(index,total):
            if total == 0:
                return True
            if index == 0:
                if arr[0] == total:
                    return True
                return False
            if dp[index][total] != -1:
                return dp[index][total]
            if arr[index] > total:
                pick = False
            else:
                pick = backtrack(index - 1,total-arr[index])
            notpick = backtrack(index - 1,total)
            dp[index][total] = pick or notpick
            return dp[index][total]
        return backtrack(len(arr)-1,sum)



# Tabulation Approach 
# TC = O(N * sum) and SC = O(N * sum)
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        dp = [[-1] * (target + 1) for _ in range(n)]

        # Base case
        for i in range(n):
            dp[i][0] = True

        if arr[0] <= target:
            dp[0][arr[0]] = True

        # Fill DP table
        for index in range(1, n):
            for total in range(1, target + 1):
                if arr[index] > total:
                    pick = False
                else:
                    pick = dp[index-1][total - arr[index]]
                notpick = dp[index - 1][total]
                dp[index][total] = pick or notpick
        return dp[n-1][target]




# Tabulation With Space Optimization 
# TC = O(N * Target) and SC = O(target)
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        prev = [False] * (target + 1)
        prev[0] = True

        if arr[0] <= target:
            prev[arr[0]] = True

        for i in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True

            for j in range(1, target + 1):
                notPick = prev[j]

                pick = False
                if arr[i] <= j:
                    pick = prev[j - arr[i]]

                curr[j] = pick or notPick

            prev = curr

        return prev[target]