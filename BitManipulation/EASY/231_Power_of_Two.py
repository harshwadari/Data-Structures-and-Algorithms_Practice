# 231 Check if a number is power of 2 or not 
# brute appraoch using convert first to binary and then check
# TC = O(logN) and SC = O(1)

def power2not(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n //2
    return n == 1


# optimal approach using bit manipulation 
# TC = O(1) and SC = O(1)

def power2(n):
    if n > 0 and (n & (n-1)) == 0:
        return True
    return False

# without bit magic 
class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1