# 992. Subarrays with K Different Integers
# brute approach by generating all subarray and checking using hashmap
# TC = O(N^2) and SC = O(N)
def kdifferent(nums,k):
    count = 0
    for i in range(len(nums)):
        map = {}
        for j in range(i,len(nums)):
            if nums[j] in map:
                map[nums[j]] +=1
            else:
                map[nums[j]] =1
            if len(map) == k:
                count +=1
            elif len(map) > k:
                break
    return count