# 239. Sliding Window Maximum

"""
You are given an array of integers nums, there
is a sliding window of size k which is moving from
the very left of the array to the very right. You
can only see the k numbers in the window. Each 
time the sliding window moves right by one position.

Return the max sliding window.
"""


# Brute approach by generating all possible answers
# TC = O(N*K) and SC = O(N)

def maxSlidingWindow(self, nums, k):
        result = []
        for i in range(len(nums)- k + 1):
            maxi = nums[i]
            for j in range(i , i + k):
                maxi = max(maxi , nums[j])
            result.append(maxi)
        return result

# Optimal approach using double ended queue
from collections import deque
# TC = O(N*K and SC = O(N)
def maxSlidingWindow(self, nums, k):
    dq = deque()
    result = []
    for i in range(len(nums)):
        # Remove out-of-window indices
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        # First window completed
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result