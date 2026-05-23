# 169 Majority Element

"""
Docstring for Arrays.Medium.2

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than 
⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# brute force method
# TC = O(N^2) and SC = O(1)


def majorityElement(self, nums):
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count +=1
            if count > n//2:
                return nums[i]
        return -1
        


# better approach
# TC = O(N) and SC = O(N)
def majo(nums):
    n = len(nums)
    map = {}
    for i in range(n):
        x = nums[i] 
        if x in map:
            map[x] +=1
        else:
            map[x] = 1
        if map[x] > n//2:
            return x
        

# moores voting algorithm more optimal
# TC = O(N) and SC = O(1)
def moores(nums):
    n = len(nums)
    count = 0
    ele = 0
    for i in range(n):
        if count == 0:
            count =1
            ele = nums[i]
        elif ele == nums[i]:
            count +=1
        else:
            count -=1

    count1 = nums.count(ele)
    if count1 > n//2:
        return ele
    return -1