# TC = O(N) and SC = O(1)

def reverseArray(nums):
    n = len(nums)
    left = 0
    right = n-1
    while left <= right:
        nums[left] , nums[right] = nums[right] , nums[left]
        left +=1
        right -=1
    return nums
print(reverseArray([1,2,3,4]))
