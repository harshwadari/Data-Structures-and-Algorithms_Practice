# . Express Number as Sum of Two Primes
"""
Given an integer n, determine whether it can be expressed as the sum of two prime numbers.

You must return true if such a pair exists, otherwise return false.

Example 1:
Input: n = 74

Output: True

Explanation: 74 = 71 + 3, and both 71 and 3 are prime numbers.

Example 2:
Input: n = 11

Output: False

Explanation: There are no two prime numbers whose sum is 11.

Constraints:
2 <= n <= 10 ^6
"""

# Brute Force Appraoch 
# TC = O(√x) and SC = O(1)
def issumofprimes(n:int) -> bool:
    def isPrime(x):
        if x < 2:
            return False
        for i in range(2,int(x ** 0.5)+1):
            if x % i == 0:
                return False
        return True
    for i in range(2,n):
        if isPrime(i) == True and isPrime(n-i) == True:
            return True
    return False

# Optimal Appraoch using sieve of erostatenus
# TC = O(NlogN) and SC = O(N)


def is_sum_of_two_primes(self, n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, n):
        if prime[i] == True and prime[n - i] == True:
            return True
    return False
