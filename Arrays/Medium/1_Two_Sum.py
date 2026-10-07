# lc 1 Two sum 
"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""


# brute force appraoch
# TC = O(N^2) and SC = O(1)
def twosum(nums,target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    


# optimal appraoch
# TC = O(N) and SC = O(N)
def twosums(nums,target):
    n = len(nums)
    hashi = {}
    for i in range(n):
        remain = target - nums[i]
        if remain in hashi:
            return [hashi[remain],i]
        hashi[nums[i]] = i


# better appraoch using two pointer
# TC = O(NLogN) and SC = O(1)

def twosum1(nums,target):
    n = len(nums)
    nums.sort()
    i = 0
    j = n-1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [i,j]
        elif s > target:
            j -=1
        else:
            i +=1 