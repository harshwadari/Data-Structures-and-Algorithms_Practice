# to find single element in a sorted array

"""
Docstring for BinarySearch.Bson1Darrays.12

You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one 
element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.


Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""

# brut appraoch using linear search and a extra data structre dictionary
# TC = O(2N) and SC = O(N)

def singlebrut(nums:list[int]) -> int:
    freq = {}
    for num in nums: # element looping
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        if freq[num] == 1:
            return num
        

# Better approach in constant space only using linear search using xor propery 
# TC = O(N) and SC = O(1)
def bettersingle(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans



# optimal approach using binary search 
# TC = O(logN) and SC = O(1)
def optimalsignal(nums):
    low = 0
    high = len(nums) -1
    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]