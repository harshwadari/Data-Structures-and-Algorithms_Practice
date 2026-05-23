# Leaders in an Array

"""
Given an integer array nums, return a list of all the leaders in the array.



A leader in an array is an element whose value is strictly greater 
than all elements to its right in the given array. The rightmost element
 is always a leader. The elements in the leader array must appear in the order they appear in the nums array.


Example 1

Input: nums = [1, 2, 5, 3, 1, 2]

Output: [5, 3, 2]

Explanation:

2 is the rightmost element, 3 is the largest element in the index range 
[3, 5], 5 is the largest element in the index range [2, 5]
"""


# brute approach using nested for loops 
# TC + = O(N^2) and SC = O(N)

def leader(nums):
    result = []

    for i in range(len(nums)):
        leaders = True
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                leaders = False
                break
        if leaders == True:
            result.append(nums[i])
    return result

# optimal approach 

""""
A leader means:

An element is greater than all elements to its right.

Instead of checking every element on the right (which gives O(N²)), think like this:

If we traverse from right → left, we already know the maximum element seen so far on the right side.

So we maintain:

max_right

Rule:

if nums[i] >= max_right
    → it is a leader
    → update max_right

Because if it is greater than everything seen so far on the right, it must be a leader.

"""

# TC = O(N) and SC = O(N)
def leaderArray(nums):
    n = len(nums)
    result = []
    maxRight = nums[n-1]
    for i in range(n-1,-1,-1):
        if nums[i] >= maxRight:
            result.append(nums[i])
            maxRight = nums[i]
    result.reverse()
    return result