# find min in roatated sorted array

#burute force using linear search

def minm(nums):
    mni = float('inf')
    for i in range(len(nums)):
        mini = min(mini,nums[i])
    return mini


# optimal using binary search
#TC = O(logN) and SC = O(1)
def binminm(nums):
    n = len(nums)
    low = 0
    mini = float('inf')
    high = n-1
    while low <= high:
        mid  = (low+high)//2
        if nums[mid] <= nums[high]:
            mini = min(mini,nums[mid])
            high = mid-1
        else:
            mini = min(mini,nums[low])
            low = mid+1
    return mini
print(binminm([4,5,6,7,0,1,2,3]))