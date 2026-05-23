# 485. Max Consecutive Ones
# TC = O(N) and SC = O(1)

def maxOnes(nums):
    n = len(nums)
    count = 0
    maxcount = 0
    for i in range(n):
        if nums[i] == 1:
            count +=1
        else:
            maxcount = max(maxcount , count)
            count = 0
    return max(maxcount , count)



# different variation

def maxONes(nums):
    n = len(nums)
    count = 0
    maxcount = 0
    for i in range(n):
        if nums[i] == 1:
            count +=1
            maxcount = max(maxcount,count)
        else:
            count = 0
    return maxcount