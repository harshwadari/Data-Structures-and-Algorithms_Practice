"""
simple funda for this
it selects the minimum element and swaps from first 
"""
# two pointer approach
def Selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[i]:
                min_idx = j
        nums[i] , nums[min_idx] = nums[min_idx],nums[i]
    return nums
print(Selection_sort([5,4,3,2,1]))
# time complexity is O(n^2)   and SC = O(1)
# n^2 is best , worst and average time complexity of selection sort       