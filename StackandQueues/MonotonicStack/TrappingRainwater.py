#Trapping Rain water

"""

Given n non-negative integers representing an elevation map where the width of each bar 
is 1, compute how much water it can trap after raining.
"""


# brute force approach 

"""
In brute force, for every bar, we calculate:

Maximum height to its left

Maximum height to its right

Water stored at that index =
min(left_max, right_max) - height[i]
"""
# TC = O(N^2) and SC = O(N)
def TrappingRainWater(height):
    n = len(height)
    total_water = 0
    for i in range(n):
        left_max = 0
        for j in range(i+1):
            left_max = max(left_max,height[j])
        right_max = 0
        for j in range(i,n):
            right_max = max(right_max,height[j])
            total_water += min(left_max,right_max) - height[i]
    return total_water


# optimal approach 
"""
Core Idea

Water depends on:

min(left_max, right_max) - height[i]

Instead of recomputing, we:

Keep two pointers: left and right

Maintain:

left_max

right_max

Move the smaller side inward

Why?

Because water is limited by the smaller boundary.
"""
# TC = O(N) and SC = O(1)
def TrappingRainWater(height):
    n = len(height)
    left, right = 0, n-1
    left_max, right_max = 0, 0
    total_water = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1
    return total_water    