"""
The Fibonacci numbers, commonly denoted F(n) form a 
sequence, called the Fibonacci sequence, such that each number 
is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""


"""
Complexities:

Method	                Time	    Space
Recursion	            O(2ⁿ)	    O(n)
Memoization	            O(n)	    O(n)
Tabulation	            O(n)	    O(n)
Space Optimized DP	    O(n)	    O(1)
Matrix Exponentiation	O(log n)	O(log n)
Fast Doubling	        O(log n)	O(log n)

For interviews:

Most companies expect the O(n), O(1) DP solution.
Matrix exponentiation is usually seen in competitive programming and advanced interviews.
If asked "Can you do better than O(n)?", then mention Matrix Exponentiation or Fast Doubling.

Fast Doubling is generally considered the cleanest 
optimal Fibonacci solution and is what competitive programmers usually use for huge n (10¹⁸+).
"""
# Optimal approach using recursion
# TC = O(2^N) and SC = O(N)
def fib(n:int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(7))


# without recursion otpimal approach using Space Optimized DP
# TC = O(N) and SC = O(1)
class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        
        return b
    
