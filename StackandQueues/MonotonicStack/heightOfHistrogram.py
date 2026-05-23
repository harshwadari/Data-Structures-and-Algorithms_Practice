# Largest Rectangle in Histogram Leetcode 84

# brute force approach using nested for loops
# TC = O(N^2) and SC = O(1)
def largestRectangleArea(heights):
    n = len(heights)
    max_area = 0
    for i in range(n):
        min_height = heights[i]
        for j in range(i,n):
            min_height = min(min_height,heights[j])
            max_area = max(max_area,min_height*(j-i+1))
    return max_area


# optimal approach using stack