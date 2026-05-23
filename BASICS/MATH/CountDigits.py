"""
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.

Example 1

Input: n = 4

Output: 1

Explanation: There is only 1 digit in 4.
"""

# pythonic approach
# TC = O(1) and SC = O(1)
def countdigits(n):
    return len(str(n))

# Logical approach using while loop
# TC = O(logN) and SC = O(1)
def countingdigits(n:int):
    if n == 0: # edge case handling if digit is zero
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count +=1
    return count 
print(countingdigits(463))