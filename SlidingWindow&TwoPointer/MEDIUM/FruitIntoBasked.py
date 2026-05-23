#Longest subarray with Atmost two distinct integers

# brute approach 
# TC = O(N^2) and SC = O(3)

def fruitbasket(nums):
    n = len(nums)
    maxlen = 0
    for i in range(n):
        myset = set()
        for j in range(i,n):
            myset.add(nums[j])
            if len(myset) <= 2:
                maxlen = max(maxlen, j - i + 1)
            else:
                break
    return maxlen


#optimal approach using sliding windows and hashing
# TC = O(N) and SC = O(1)

def frutiibasket(nums):
    n = len(nums)
    map = {}
    maxlen = 0
    left = 0
    for right in range(n):
        if nums[right] in map:
            map[nums[right]] +=1
        else:
            map[nums[right]] =1
        while len(map) <= 2:
            map[nums[left]] -=1
            if map[nums[left]] == 0:
                del map[nums[left]]
            left +=1
        maxlen = max(maxlen,right - left + 1)
    return maxlen