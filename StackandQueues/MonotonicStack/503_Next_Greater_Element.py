# 503. Next Greater Element II
# TC = O(N) and SC = O(N)
def nextGreaterElements(self, nums):
    n = len(nums)
    stack = []
    result = [-1] * n
    for i in range(2 * n-1,-1,-1):
        while len(stack) != 0 and nums[stack[-1]] <= nums[i%n]:
            stack.pop()
        if i < n:
            if len(stack) != 0:
                result[i] = nums[stack[-1]]
        stack.append(i % n)
    return result