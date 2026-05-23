# 1423. Maximum Points You Can Obtain from Cards


# optimal solution using prfix sum and sliding window 

def cardpoints(nums,k):
    n = len(nums)
    leftsum = 0
    rightsum = 0
    maxsum = 0
    for i in range(k):
        leftsum += nums[i]
        maxsum = leftsum
    rightindex = len(nums) - 1
    for i in range(k-1,-1,-1):
        leftsum  = leftsum  - nums[i]
        rightsum = rightsum + nums[rightindex]
        maxsum = max(maxsum , rightsum + leftsum)
    return maxsum 