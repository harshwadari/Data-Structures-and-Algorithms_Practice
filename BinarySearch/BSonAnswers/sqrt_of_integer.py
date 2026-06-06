# Square Root
"""
Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.
Floor value of any number is the greatest Integer which is less than or equal to that number.
"""
# https://www.geeksforgeeks.org/problems/square-root/1
# approach using built in python math function
#TC = O(N) for float value and for floor TC = O(logN) and SC = O(1)
import math 
def floorsqrt(n):
    return math.isqrt(n) # for float value math.sqrt(n) where n is an integer


# better appraoch using linear traversing 
# TC = O(N) and SC = O(1)

def linearsqrt(n):
    for i in range(n):
        if i * i <= n:
            result = i
        else:
            break
    return result

# otpimal appraoch using binary search on answer space
# TC = O(logn) and SC = (1)

def bsSqrt(n):
    low = 1
    high = n
    result = 1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid > n :
            high = mid - 1
        else:
            low = mid + 1
            result = mid
    return mid 