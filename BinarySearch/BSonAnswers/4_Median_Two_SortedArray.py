# To find median of two sorted array

"""
Docstring for BinarySearch.BSonAnswers.2
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

 
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""



# exteme Niave approach 
# TC = O(N + M) and SC = O(N + M )
def medianOf2(self, a, b):
        # code here
        result = a + b
        result.sort()
        if len(result) %2 == 1:
            return result[len(result)//2]
        return (result[len(result)//2 -1] + result[len(result)//2])/ 2.0








# brut force approach merge two sorted if len of merged arr is even n//2 else one formula
# TC = O(N+M) and SC = O(N+M)
def medsort(nums1 : list[int],nums2 : list[int])-> float:
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    merged = []
    while i < n and j <m:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i +=1
        else:
            merged.append(nums2[j])
            j +=1
    while i < n:
        merged.append(nums1[i])
        i +=1
    while j <m:
        merged.append(nums2[j])
        j +=1
    r = len(merged)
    if r%2 == 1: # this tells odd
        return merged[r//2]
    else:
        return (merged[r//2-1] + merged[r//2])/2.0
print(medsort([1,2],[3,4]))



# better approach using two pointer 

def midsort(nums1,nums2):
    i = 0
    j = 0
    


# optimal using parationing binary search

def binmedsort(nums1,nums2):
    pass