# 53. maxsummum Subarray

"""
Docstring for Arrays.Medium.3

Given an integer array nums, find the subarray with the largest sum, and return its sum.
 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
"""


# brute force

# TC = O(N^2) and SC = O(1)
def kadane(nums): 
    n = len(nums)
    maxsum = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            maxsum = max(maxsum,sum )
    return maxsum 



# optimal 
# TC = O(N) and SC = O(1)
def kadanee(nums):
    n = len(nums)
    sum = 0
    maxsum = nums[0]
    for i in range(n):
        sum += nums[i]
        maxsum = max(maxsum,sum)
        if sum <0:
            sum = 0
    return maxsum




"""

I use Kadane's Algorithm. While iterating the array, I maintain 
the maxsummum subarray ending at the current index. If the previous 
sum becomes negative, I start a new subarray from the current element. 
I keep updating the global maxsummum. This gives an O(n) time and O(1) space solution.





Intuition (short)

At every index we decide:

continue the previous subarray
OR
start a new subarray from current element

If the previous sum becomes negative, it will only reduce future sums, so we reset it.

Optimal Idea (Kadane’s Algorithm)

Keep two variables:

current_sum → sum of current subarray
max_sum → best answer found so far

At each element:

current_sum = max(nums[i], current_sum + nums[i])
max_sum = max(max_sum, current_sum)
"""