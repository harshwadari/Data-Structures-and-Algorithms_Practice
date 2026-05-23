# Find the repeating and missing number

"""
Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.



Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.



Note: You are not allowed to modify the original array.


Example 1

Input: nums = [3, 5, 4, 1, 1]

Output: [1, 2]

Explanation:

1 appears two times in the array and 2 is missing from nums
"""


# brute code 
# TC = O(N^2) and SC = O(1)
def findMissingRepeatingNumbers(self, nums):
        missing = -1
        repeating = -1
        n = len(nums)
        for i in range(1,n+1):
            count = 0
            for j in range(n):
                if nums[j] == i:
                    count +=1
            if count ==2:
                repeating = i
            elif count ==0:
                missing = i
        return [repeating,missing]


"""
Better Approach (Hash / Frequency Array)
Idea

Since numbers are 1 → n, create a frequency array of size n+1.

Count frequency of every element.

freq[i] = 2 → repeating

freq[i] = 0 → missing
"""
# TC = O(N) and SC = O(N)
def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        missing = -1
        repeating = -1
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] =1
        for i in range(1 , n+1):
            if i in freq and freq[i] ==2:
                repeating = i
            elif i not in freq:
                missing = nums[i]

        return [repeating, missing]


"""
Optimal Approach (Math Formula)

Uses:

sum of first n numbers

sum of squares

Idea

Expected values

S  = n(n+1)/2
S2 = n(n+1)(2n+1)/6

Let

x = repeating
y = missing

Actual array

sum(arr)  = S + x - y
sum(arr²) = S2 + x² - y²

So

x - y = diff1
x² - y² = diff2

And

x² - y² = (x-y)(x+y)

So we can find x and y.
"""

# TC = O(N) and SC = O(1)
def findTwoElement(arr, n):

    S = n*(n+1)//2
    S2 = n*(n+1)*(2*n+1)//6

    arr_sum = sum(arr)
    arr_sq_sum = sum(x*x for x in arr)

    diff1 = arr_sum - S          # x - y
    diff2 = arr_sq_sum - S2      # x² - y²

    sum_xy = diff2 // diff1      # x + y

    repeating = (diff1 + sum_xy)//2
    missing = repeating - diff1

    return repeating, missing