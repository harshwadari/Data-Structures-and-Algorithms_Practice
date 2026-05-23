# to rotate array by left place one 
#TC = O(N) and SC = O(n)
def rot(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(1,n):
        nums[i-1] = nums[i]
    nums[len(nums)-1] = temp
    return nums
print(rot([1,2,3,4,5]))