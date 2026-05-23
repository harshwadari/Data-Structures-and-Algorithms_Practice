# merge sort 
# it just  divide array till one element and sort array
# TC = O(nlogN) sc = O(n)
def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    # Merge until one array is exhausted
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements from left (if any)
    while i < n:
        result.append(left[i])
        i += 1

    # Append remaining elements from right (if any)
    while j < m:
        result.append(right[j])
        j += 1

    return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid= len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_arr(left,right)
print(merge_sort([10,9,8,7,6,5,4,3,2,1]))