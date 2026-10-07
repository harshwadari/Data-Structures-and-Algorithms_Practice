#88. Merge Sorted Array

"""
Brute Force
Idea

Copy nums2 elements into the empty space of nums1

Sort nums1Intuition

Just combine everything and sort.
"""
# Brute code 
# TC = O(((m+n) log(m+n))) SC = O(1)

class Solution:
    def merge(self, nums1, m, nums2, n):
        
        # copy nums2 into nums1
        for i in range(n):
            nums1[m+i] = nums2[i]

        # sort the array
        nums1.sort()


"""
Better Approach (Extra Array)
Idea

Use two pointers and build a new array.

Compare elements of both arrays

Insert smaller one

Continue until finished
"""

# TC = O(M+N) and SC = 0(M+N)
def mergebetter(nums1 , m , nums2, n):
    i = 0
    j = 0
    result = []
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i +=1
        else:
            result.append(nums2[j])
            j +=1
    while i < m:
        result.append(nums1[i])
        i +=1
    while j < n:
        result.append(nums2[j])
        j +=1
    for  i in range(m+n):
        nums1[i] = result[i]


"""
Optimal Approach (Two Pointer from Back) 

This is the interview expected solution.

Key Idea

Fill nums1 from the back.

Why?

Because the end of nums1 is empty.

We place the largest element at the end first.

Algorithm

Pointers:

i = m-1  (last valid element of nums1)
j = n-1  (last element of nums2)
k = m+n-1 (last index of nums1)

Compare from back and place the larger element.
"""

# TC = O(M+N) and SC = O(1)
def mergeoptimal(nums1,m,nums2,n):
    i  = m-1
    j = n-1
    k = m+n -1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j -=1
        k -=1
    while j >=0:
        nums1[k] = nums2[j]
        j -=1
        k -=1
