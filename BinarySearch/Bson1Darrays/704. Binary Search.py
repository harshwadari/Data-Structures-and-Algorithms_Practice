# Linear Search
# TC = O(N) and SC = O(1)

def ls(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1
print(ls([1,2,3,4,5],9))


# Binary Search
# TC = O(logN) and SC = O(1)
def bs(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1
print(bs([1,2,3,4,5,6,7,8,9],6))