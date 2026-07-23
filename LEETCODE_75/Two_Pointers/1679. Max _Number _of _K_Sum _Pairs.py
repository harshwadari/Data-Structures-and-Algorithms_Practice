# 1679. Max Number of K-Sum Pairs
"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k 
and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

# Brute Force Approach using Nested Loops
# TC = O(N^2) and SC = O(N) visited Arr
class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i]:
                continue

            for j in range(i + 1, len(nums)):
                if not visited[j] and nums[i] + nums[j] == k:
                    count += 1
                    visited[i] = True
                    visited[j] = True
                    break

        return count


# Optimal Appraoch  using Two Pointer
# TC = O(NlogN) and SC = O(1)
def kSum(nums:list[int] , k:int) -> int:
    count = 0
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        total = nums[i] + nums[j]
        if total == k:
            count += 1
            i += 1
            j -= 1
        elif total < k:
            i += 1
        else:
            j -= 1
    return count 


# Different Optimal Approach using Hahmap
# TC = O(N) and SC = O(N)
def hashmapSumk(nums,k):
    count = {}
    operations = 0
    
    for num in nums:
        complement = k - num
    
        if complement in count and count[complement] > 0:
            operations += 1
            count[complement] -= 1
        else:
            count[num] = count.get(num, 0) + 1
    
    return operations