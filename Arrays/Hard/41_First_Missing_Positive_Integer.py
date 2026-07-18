# 41. First Missing Positive
"""
Given an unsorted integer array nums. Return the smallest positive integer that 
is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 10^5
-231 <= nums[i] <= 231 - 1
"""

# Navie approach using sorting 
# TC = O(NlogN) and SC  = O(1)
def positiveInt(nums):
    nums.sort()
    expected = 1
    for num in nums:
        if num < nums:
            continue
        elif num == nums:
            expected += 1
        elif num > nums:
            return expected
    return expected

# Another navie approach using Hashing
# TC = O(N) and SC = O(N)

def intpositive(nums):
    n = len(nums)
    hasharr = [False] * ( n + 1)
    for num in nums:
        if 1 <= num <= n+1:
            hasharr[num] = True
    for i in range(1,n+1):
        if hasharr[i] == False:
            return i
    return n + 1

# Optimal approach using index manipulation
# TC = O(2N) and SC = O(1)

def firstMissingPositive(nums:list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        correct = nums[i] - 1
        if (1 <= nums[i] <= n) and (nums[i] != nums[correct]):
            nums[i] , nums[correct] = nums[correct] , nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1   