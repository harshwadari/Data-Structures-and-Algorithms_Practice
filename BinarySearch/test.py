def SelectionSort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j] < nums[min_idx]:
                min_idx = j
            nums[i] , nums[min_idx] = nums[min_idx] , nums[i]
    return nums
print(SelectionSort([5,4,3,2,1]))




def bubbleSort(nums):
    n =len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                swapped = True
            nums[j] , nums[j+1] = nums[j+1] , nums[j]
        if not swapped:
            break
    return nums
print(bubbleSort([5,4,3,2,1]))


def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        key  = nums[i]
        j = i-1
        while j >=0 and nums[j] >key:
            nums[j+1] = nums[j]
            j = j-1
        nums[j+1] = key
    return nums
print(insertionSort([5,4,3,2,1]))

