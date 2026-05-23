# Count Inversion

"""
Given an integer array nums. Return the number of inversions in the array.



Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.



It indicates how close an array is to being sorted.


A sorted array has an inversion count of 0.


An array sorted in descending order has maximum inversion.

Example 1

Input: nums = [2, 3, 7, 1, 3, 5]

Output: 5
"""



# brute force  use nested for loop
# TC = O(N^2) and SC = O(1)
def countInversion(nums):
    count = 0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                count +=1
    return count


# optimal code 

"""

The optimal way to count inversions is using Merge Sort.

Reason:
When we merge two sorted halves, we can detect how many elements from the left are greater than the current element from the right. Instead of checking pairs one-by-one, we count them in bulk.

Time Complexity becomes O(N log N) instead of O(N²)

Intuition

Suppose the array is:

[5, 3, 2, 4, 1]

Divide it like merge sort:

[5,3,2] | [4,1]

Eventually we reach sorted halves:

Left  = [2,3,5]
Right = [1,4]

During merge:

2 3 5
1 4

Compare:

2 > 1

Since the left array is sorted, if 2 > 1 then:

3 > 1
5 > 1

So we instantly know 3 inversions.

Instead of checking individually, we add:

len(left) - i

This is the core trick.
"""

