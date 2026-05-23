# Jump Game 2 lc 45

# Optimal solution using greedy / two pointer approach 
# TC = O(N) and SC = O(1)
def jumpingGame(nums):
    left = 0
    right = 0
    n = len(nums)
    jump = 0
    while right < n - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest , i + nums[i])
        left = right + 1
        right = farthest
        jump += 1
    return jump 
