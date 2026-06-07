# find the floor and ciel of array
"""
Docstring for BinarySearch.5
Problem Statement: ou're given an sorted array arr of n 
integers and an integer x. Find the floor and ceiling of x 
in arr[0..n-1]. The floor of x is the largest element in the
array which is smaller than or equal to x. The ceiling of x is the 
smallest element in the array greater than or equal to x



Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and 
the ceiling of 5 in the array is 7.
"""


#optimal appraoch using lower and upper bound
#TC = O(logN) and SC = O(1)
def getfloorCeil(nums,target):
    floor = -1
    ceil = -1
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return [nums[mid],nums[mid]]
        elif nums[mid] > target:
            ceil  = nums[mid]
            high = mid-1
        else :
            floor = nums[mid]
            low = mid+1
    return [floor,ceil]