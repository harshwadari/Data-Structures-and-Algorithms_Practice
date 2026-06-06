# 2574. Left and Right Sum Differences

# arr = [10,4,8,3]

# left = [0] * len(arr)
# right = [0] * len(arr)

# # left sums
# for i in range(1, len(arr)):
#     left[i] = left[i - 1] + arr[i - 1]

# # right sums
# for i in range(len(arr) - 2, -1, -1):
#     right[i] = right[i + 1] + arr[i + 1]


# TC = O(3N) and SC = O(N)
def leftRightDiff(nums):
    n = len(nums)
    leftsum = [0] * n
    rightsum = [0] * n
    for i in range(1,n):
        leftsum[i] = leftsum[i - 1] + nums[i - 1]
    for i in range(n-2 , -1 , -1):
        rightsum[i] = rightsum[i + 1] + nums[i + 1]
    result = []
    for i in range(n):
        result.append(abs(leftsum[i] - rightsum[i]))
    return result