# Next permutation 

"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
"""



# brute approach
# TC = O(N*N!)
#intiuition

"""
generate all sorted permutaiton using recursion
linear seach
next permutation
"""


# optimal approach 

"""
1.first find pivot element in array 
pivot element is arr[i] < arr[i+1] form bakwards
2.find rightmost element greater than pivot
then swap rightmost and pivot
3.reverse (pivot+1) - n-1
"""


"""
We scan from the right to find the first decreasing point
because everything after it is already in descending order 
(largest permutation). We swap that element with the next 
greater element on the right to make the number slightly 
larger, and then reverse the suffix to get the smallest arrangement after it.
"""

# TC = O(3N) and SC = O(1)
def nextpermutataion(nums):
    n = len(nums)
    # find pivot element
    i = n-2
    while i >=0 and nums[i] >= nums[i+1]:
        i -=1
    # swap pivot wiht the rightmost element
    if i >=0:
        j = n-1
        while nums[j] <= nums[i]:
            j -=1
        nums[i] , nums[j] = nums[j] , nums[i]
    # reverse remaining
    left = i+1
    right  = n-1
    while left < right:
        nums[left] , nums[right] = nums[right], nums[left]
        left +=1
        right -=1
    return nums
print(nextpermutataion([1,2,5,4,3]))