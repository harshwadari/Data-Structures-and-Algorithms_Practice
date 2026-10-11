# 204 Count Primes
"""
Given an integer n, return the number of prime numbers that are strictly 
less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""


# Brute force appraoch 
# TC = O(n root n) and sc = O(1)
class Solution(object):
    def countPrimes(self, n):
        count = 0

        for num in range(2, n):
            is_prime = True

            i = 2
            while i * i <= num:
                if num % i == 0:
                    is_prime = False
                    break
                i += 1

            if is_prime:
                count += 1

        return count


# Otpimal Appraoch using sieve of erostatenus 
# TC = O(NlogN) and SC = O(1)
