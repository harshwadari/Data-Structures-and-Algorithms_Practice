"""
simple funda 
it pushes the max element to last by adjacent swap 
"""
def Bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
         if nums[j] > nums[j+1]:
            nums[j], nums[j+1]= nums[j+1],nums[j]  
        swapped = True
        if not swapped:
          break
    return nums
print(Bubble_sort([100,1,7,99,2,3,0]))
#time complexity is O(n^2)
# best case is O(n)
