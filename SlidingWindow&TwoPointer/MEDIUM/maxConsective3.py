# Max Consecutive Ones part 3 

# brute approach using nested loops
# TC = O(N^2) and SC = O(1)
def maxconsecOnes(nums, k):
    n = len(nums)
    maxlen = 0
    for i in range(n):
        zeros = 0
        for j in range(i,n):
            if nums[j] == 0:
                zeros +=1
            if zeros <= k:
                leng = j - i + 1
                maxlen = max(maxlen, leng)
            else:
                break
    return maxlen

# optimal approach
# TC = O(N) and SC = O(1)
def maxOnes(nums,k):
    n = len(nums)
    left = 0
    maxlen = 0
    zeros = 0
    for right in range(n):
        if nums[right] == 0:
            zeros +=1
        while zeros > k:
            if nums[left] == 0:
                zeros -=1
            left +=1
        maxlen = max(maxlen, right - left + 1)
    return maxlen

