# to  remove duplicates from an array

# optimal approach

def duplicates(nums):
    n = len(nums)
    i = 0
    for j in range(1,n):
        if nums[j]!= nums[i]:
            nums[i+1] = nums[j]
            i +=1
    return i+1


# gfg to remove duplicates from a sorted array

def remove(nums):
    n = len(nums)
    if n == 0:
        return []
    i = 0
    for j in range(1,n):
        if nums[j] != nums[i]:
            i +=1
            nums[i] = nums[j]
    return nums[:i+1]



def remSorted(nums):
    n = len(nums)
    my_set = set()
    for i in range(n):
        my_set.add(nums[i])
    return my_set
