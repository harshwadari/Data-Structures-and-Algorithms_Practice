# find out how many times arr is rotated

# brut first we have to fin min the return min index

def brut(nums):
    return min(nums)

# better brute

def better(nums):
    mini = nums[0]
    for i in range(len(nums)):
        if nums[i] < mini:
            mini = nums[i]
    return mini
print(better([5,4,3,1,8]))


# optimal approach using binary search same as find min in rotated sorted array

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