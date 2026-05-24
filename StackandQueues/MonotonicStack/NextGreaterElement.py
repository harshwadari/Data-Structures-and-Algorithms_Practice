#Next Greater Element Leetcode  496

# brut force approach using nested for loops
# TC = O(N^2) and SC = O(N)
def nextGreaterElement(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    result = [-1]*n
    for i in range(n):
        for j in range(m):
            if nums1[i] == nums2[j]:
                for k in range(j+1,m):
                    if nums2[k] > nums1[i]:
                        result[i] = nums2[k]
                        break
                break
    return result


# optimal approach using monotonic stack
# TC = O(2N) and SC = O(N)
def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    result = []
    for num in nums1:
        result.append(next_greater.get(num, -1))
    return result








# next greater element in gfg
# brute force approach using nested for loops
# TC = O(N^2) and SC = O(N)
def nextGreaterElement(arr):
    n = len(arr)
    result = [-1]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    return result

# optimal approach using monotonic stack
# TC = O(2N) and SC = O(N)
def nextGreaterElement(arr):
    stack = []
    result = [-1]*len(arr)
    for i in range(len(arr)):
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) != 0:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result
