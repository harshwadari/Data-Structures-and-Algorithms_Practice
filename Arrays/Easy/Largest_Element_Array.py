# To find the largest element in an array



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


# TC = O(N) and SC = O(1)
def largesttt(nums):
    return max(nums)