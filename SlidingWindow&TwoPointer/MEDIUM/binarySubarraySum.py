# Binary Subarrarray with sum

# brut force approach using nested for loops
# TC = O(N ^2) and SC = O(1)

def binarysubarray(nums,goals):
    n = len(nums)
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            if sum == goals:
                count +=1
    return count

# Optimal approach 
# TC = O(2N) and SC = O(1)
def binarysum(nums,goal):
    return atmost(nums,goal) - atmost(nums,goal - 1)    
def atmost(nums,goal):
    if goal < 0:
        return 0
    sum = 0
    count = 0
    n = len(nums)
    left = 0
    for right in range(n):
        sum += nums[right]
        while sum  > goal:
            sum -= nums[left]
            left +=1
        count += right - left + 1
    return count