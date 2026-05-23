"""
Docstring for leetcode.75
Given an array nums with n objects colored red, white, or blue, sort
 them in-place so that objects of the same color are adjacent, with the
   colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white,
 and blue, respectively.

You must solve this problem without using the library's sort function
"""


# extreme naive brute force method 
# using built in function
# TC  = O(NlogN) and SC = O(1)

def sortColor(nums):
    nums.sort()
    return nums
print(sortColor([2,0,2,1,1,0]))



# better appraoch using count sort algo
# TC = O(4N) and SC = O(1)

def SortColors(nums):
    n = len(nums)
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(n):
        if nums[i] == 0:
            count1 +=1
        elif nums[i] ==1:
            count2 +=1
        else:
            count3 +=1
    i = 0
    while count1 > 0:
        nums[i] = 0
        i +=1
        count1 -=1
    while count2 >0:
        nums[i] =1
        i +=1
        count2 -=1
    while  count3 >0:
        nums[i] =2
        i +=1
        count3 -=1
    return nums
print(SortColors([2,0,2,1,1,0]))



# most optimal method using Dutch National Flag Algorithm
# TC = O(N) and SC = O(1)

def SortingColors(nums:list[int])->list[int]:
    n = len(nums)
    l = 0
    m = 0
    h = n-1
    while m <= h:
        if nums[m] == 0:
            nums[l] , nums[m] = nums[m] , nums[l]
            l +=1
            m +=1
        elif nums[m] ==1:
            m +=1
        else:
            nums[m] , nums[h] = nums[h], nums[l]
            h -=1
    return nums
print(SortingColors([2,0,2,1,1,0]))