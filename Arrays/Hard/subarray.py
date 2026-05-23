# code to print all subarrays

def subarray(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            for k in range(i,j+1):
                print(nums[k],end="")
        print()
print(subarray([1,2,3,4,5]))
            