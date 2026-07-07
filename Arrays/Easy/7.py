# to move zeroes to end in an array
# brut force approach
#TC = O(N^2) and SC = O(N)
def zero(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] ==0:
            for j in range(i+1,n):
                nums[j-1] = nums[j]
            nums[n-1] = 0
    return nums
print(zero([1,2,0,3,4,0,9]))


# better approach using a temp arr

def zero1(nums):
    n = len(nums)
    temp = []
    for x in nums:
        if x!=0:
            temp.append(x)
    
    zero_count = n- len(temp)
    for i in range(n):
        temp.append(0)

# Optimal approach using two pointer
# TC = O(N) and SC = O(1)
def moveZeroesnums (nums:list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1