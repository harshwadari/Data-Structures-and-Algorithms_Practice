# K-th element of two Arrays


# extreme Naive approach 
def kthele(nums1,nums2, k):
    result = nums1 + nums2
    result.sort()
    return result[k - 1]
# brute approach
"""
apply merge sort logic on both arrays and form sorted in resutl array 
"""

# TC = O((n + m) log(n + m)) and SC = O(N + M )
def kthElement( a, b, k):
    m = len(a)
    n = len(b)
    i = 0
    result = []
    j = 0
    while i < m and j < n:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < m:
        result.append(a[i])
        i += 1
    while j < n:
        result.append(b[j])
        j += 1
    return result[k - 1]



# Better Apprach using two pointer 
# TC = O(N) and SC = O(1)

def kthbetter(nums1: list[int], nums2:list[int],k:int) -> int:
    pass

# Optimal appraoch using binary seach partition
# TC = O(log(min(a,b))) where a and b is two sorted arrays and sc is O(1)

def kthoptimal(nums1:list[int], nums2:list[int],k:int) -> int:
    pass 
