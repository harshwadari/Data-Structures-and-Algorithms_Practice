#Implement Lower Bound

'''

lower bound is smallest index which is nums[i] >= target
lower bound is the first occurrence of target in the sorted array
if target is not present in the array then it will return the index of the next greater element
Example 1
Input: nums = [1,2,2,3,3,3,4,5], target = 3
Output: 3
'''
# TC = O(logN) and SC = O(N)
def lowerBound(nums,target):
    n =len(nums)
    lb = n
    low = 0
    high = n-1
    while low <=high:
        mid = (low+high)//2
        if nums[mid] >=target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
print(lowerBound([1,2,2,3,3,3,4,5],3)) 
