# Recursive approach 
def mincost(arr,k):
    n = len(arr)
    def backtrack(index):
        if index == 0:
            return 0 
        ans = float('inf')
        for i in range(1,k+1):
            if index - i >= 0:
                jumps = backtrack(index -1 ) + abs(arr[index] - arr[index - i])
                ans = min(jumps,ans)
        return ans
    return backtrack(n -1)


# memoization appraoch 
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        dp = [-1] * n
        def backtrack(index):
            if index == 0:
                return 0 
            ans = float('inf')
            if dp[index] != -1:
                return dp[index]
            for i in range(1,k+1):
                if index - i >= 0:
                    jumps = backtrack(index -i ) + abs(arr[index] - arr[index - i])
                    ans = min(jumps,ans)
            dp[index] = ans
            return dp[index]
        return backtrack(n -1)    
    
# Tabulatiom appraoch 
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)

        dp = [0] * n
        dp[0] = 0

        for i in range(1, n):
            ans = float('inf')

            for j in range(1, k + 1):
                if i - j >= 0:
                    jumps = dp[i - j] + abs(arr[i] - arr[i - j])
                    ans = min(ans, jumps)

            dp[i] = ans

        return dp[n - 1]