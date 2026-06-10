# to check given array is sorted or not 
#TC = O(N) and SC = O(1)
def isSort(nums):
    n = len(nums)
    for i in range(1,n):
        if nums[i] < nums[i-1]:
            return False
    return True
print(isSort([1,2,3]))



#leetcode 1752
# to check given array is sorted and rotated

def isRot(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            count +=1
            return False
    return True