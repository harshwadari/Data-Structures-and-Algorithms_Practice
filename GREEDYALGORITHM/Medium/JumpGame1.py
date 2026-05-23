# Jump Game 1 lc 55
# TC = O(N) and SC = O(1)
def Jumpgame(nums):
    maxIndex = 0
    for i in range(len(nums)):
        if i > maxIndex:
            return False
        maxIndex = max(maxIndex , i + nums[i])
    return True