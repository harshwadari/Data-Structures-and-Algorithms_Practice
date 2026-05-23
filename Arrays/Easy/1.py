# To find the largest element in an array

#https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1?page=1&category=Arrays&sortBy=submissions

# brute appraoch
#SC = O(NlogN) and SC =O(1)

def largestele(nums):
    nums.sort()
    return nums[len(nums)-1]
print(largestele([1,2,3,4,5]))

# better approach
# TC = O(N^2) and SC = O(1)


def largestElement(arr):
    n = len(arr)
    for i in range(n):
        is_largest = True
        for j in range(n):
            if arr[j] > arr[i]:
                is_largest = False
                break
        if is_largest:
            return arr[i]



#optimal approach
# TC = O(N) and SC = O(1)

def isLargest(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(n):
        if nums[i] > largest:
            largest = nums[i]
    return largest