#  Count Occurrences in a Sorted Array

"""
Docstring for BinarySearch.7

You are given a sorted array of integers arr and an integer target.
 Your task is to determine how many times target appears in arr.
Return the count of occurrences of target in the array.


Example 1

Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1

Output: 3

Explanation: The number 1 appears 3 times in the array.
"""



# brute force approach using linear seach
#TC = O(N) and SC = O(1)
def counting(nums,target):
    count = 0
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
    return count



# optimal approach using binary search

def countOccurences(arr,target):
        n = len(arr)
        low = 0
        high = n-1
        first = -1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] >= target:
                if arr[mid] == target:
                    first = mid
                high = mid-1
            else:
                low = mid+1
        if first ==-1:
            return 0
        last = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] <= target:
                if arr[mid] == target:
                    last = mid
                low = mid+1
            else:
                high = mid-1
        return last -first +1
print(countOccurences([0, 0, 1, 1, 1, 2, 3],1))
