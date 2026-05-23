# painters partition problem
# https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

# optimal approach using binary search on answers
# TC = O(logN) and SC = O(1)
def painter(nums,k):
    left = max(nums)
    right = sum(nums)
    while left < right :
        mid = (left + right) // 2
        if isvalid(nums,k,mid):
            right = mid
        else:
            left = mid + 1
    return left
def isvalid(nums,k,maxsum):
    count = 1
    curr = 0
    for num in nums:
        if curr + num > maxsum:
            count += 1
            curr = num
        else:
            curr += num
    return count <= k