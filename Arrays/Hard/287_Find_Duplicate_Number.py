# 287. Find the Duplicate Number
"""
Given an array of integers nums containing n + 1 integers where each integer is 
in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only 
constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer 
which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""


# Hash Map Appraoch 
# TC = O(2N) and SC = O(N)
def mapDuplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for key,values in freq.items():
        if values > 1:
            return key


# Hash Set Appraoch 
# TC = O(N) and SC = O(N)
def setDuplicate(nums):
    myset = set()
    for num in nums:
        if num in myset:
            return num
        else:
            myset.add(num)



# Binary Seach Appraoch 
# TC = O(NlogN) and SC = O(1)
def binaryDuplicate(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        count = 0
        mid = (low + high) // 2
        for num in nums:
            if num <= mid:
                count += 1
        if count > mid:
            high = mid 
        else:
            low = mid + 1
    return  low 




# Sorting Appraoch 
# TC = O(Nlogn) and SC = O(1)
def SortingDuplicate(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]




# Optimal Approach Using Floyd Cycle Detection Algorithm
# TC = O(2N) and SC = O(1)
def FloydDuplicate(nums:list[int]) -> int:
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow