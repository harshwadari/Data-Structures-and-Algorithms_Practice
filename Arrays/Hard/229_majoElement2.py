# 229. Majority Element II

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
"""


# brute force 
# TC = O(N^2) and SC = O(N)

def majorityElement(nums):
    n = len(nums)
    result = []

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1

        if count > n//3 and nums[i] not in result:
            result.append(nums[i])

    return result




# better approach using hash map dictionary
# TC = O(N) and SC = O(N)

def majorityElement(nums):
    n = len(nums)
    result = []
    map = {}
    for i in range(n):
        x = nums[i]
        if x in map:
            map[x] += 1
        else:
            map[x] = 1

    for key, value in map.items():
        if value > n//3:
            result.append(key)

    return result



# moores voting algorithm
# TC = O(N) and SC = O(1)

def majorityElement(nums):
    n = len(nums)
    count1 = 0
    count2 = 0
    ele1 = None
    ele2 = None

    for i in range(n):
        if count1 == 0 and nums[i] != ele2:
            count1 = 1
            ele1 = nums[i]
        elif count2 == 0 and nums[i] != ele1:
            count2 = 1
            ele2 = nums[i]
        elif nums[i] == ele1:
            count1 += 1
        elif nums[i] == ele2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    if nums.count(ele1) > n//3:
        result.append(ele1)
    if nums.count(ele2) > n//3:
        result.append(ele2)

    return result


"""
Since elements must appear more than n/3, there can be at most two such elements,
so we track two candidates and cancel others using Moore’s voting idea, then verify their counts.
"""