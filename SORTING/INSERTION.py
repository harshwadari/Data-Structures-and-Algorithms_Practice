#Insertion Sorting algorithm 

"""
simeple funda for this 
Takes an element and place it in it's current position
"""

arr = [5,4,3,2,1]
arr.sort()
print(arr)


# TC = O(N^2) and SC = O(1)
def Insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]  
        j = i-1
        while j >= 0 and nums[j]>key:
         nums[j+1] = nums[j]
         j = j-1
         nums[j+1] = key
    return nums
print(Insertion_sort([5,4,3,2,1]))