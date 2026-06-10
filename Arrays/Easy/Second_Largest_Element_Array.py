# to find second largest element in array
# brut force method
# TC = O(NlogN) and SC = O(1)
def s2largest(nums) :
    nums.sort()
    return nums[len(nums)-2]
print(s2largest([1,2,3,4,5]))


# better apprach
# TC = O(2N) and SC = O(1)
def secondLargest(nums):
    n = len(nums)
    largest = nums[0]
    slargest = -1
    for i in range(n):
        if nums[i] > largest:
            largest = nums[i]
    for i in range(n):
        if nums[i] > slargest and nums[i] != largest:
            slargest = nums[i]
    return slargest
print(secondLargest([1,2,3,4,5]))


# better appraoch
# TC = O(N) and SC = O(1)

def optlargest(nums):
    largest = -1
    slargest = -1
    for num in nums:
        if num > largest:
            slargest= largest
            largest = num
        elif num < largest and num > slargest:
            slargest = num
    return slargest
print(optlargest([1,2,3,4,5]))




# to find kth largest element in array

# brute force appraoch 
# TC = O(Nlog N) and SC = O(1)
def klargest(nums,k):
    nums.sort()
    return nums[len(nums)-k]


# better appraoch 
#TC = O() and SC O()

# Heaps(Priority Queue) concept required
