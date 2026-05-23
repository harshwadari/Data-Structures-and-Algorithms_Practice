# Max Product Subarray

"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


# brute force approach
"""
Intuition 
use two pointer nested loop find max product
"""
# TC = O(N^2) and SC = O(1)

def maxProduct(nums):
    maxproduct = nums[0]
    for i in range(len(nums)):
        product = 1
        for j in range(i,len(nums)):
            product *= nums[j]
            maxproduct = max(maxproduct,product)
    return maxproduct
print(maxProduct([4, 5, 3, 7, 1, 2]))




# optimal approach
"""
Intuition

Pattern

It falls under:

Prefix / Suffix product scanning

You scan the array from left and from right because zeros and negative numbers break the product chain.

Intuition

Two things break product subarrays:

 Zero → resets product
 Odd number of negatives

Example:

nums = [-1, -2, -3]

Whole product:

-1 * -2 * -3 = -6

But best subarray is:

[-2, -3] = 6

This happens because removing one negative from left or right can make product positive.

So we check:

product from left → prefix

product from right → suffix
"""



#optimal approach using suffix and prefix pattern
# TC = O(N) and SC = O(1)

def maxiproduct(nums):
    suffix = 0
    prefix = 0
    maxproduct = nums[0]
    for i in range(len(nums)):
        if suffix == 0:
            suffix = 1
        if prefix ==0:
            prefix =1
        prefix *= nums[i]
        suffix *= nums[len(nums)-i-1]
        maxproduct = max(maxproduct,max(prefix,suffix))
    return maxproduct
print(maxiproduct([4, 5, 3, 7, 1, 2]))