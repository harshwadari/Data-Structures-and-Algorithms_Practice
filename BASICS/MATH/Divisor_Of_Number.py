# 690. Divisors of a Number
"""
You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.

A number which completely divides another number is called it's divisor.

Example 1:
Input: n = 6

Output = [1, 2, 3, 6]

Explanation: The divisors of 6 are 1, 2, 3, 6.

Example 2:
Input: n = 8

Output: [1, 2, 4, 8]

Explanation: The divisors of 8 are 1, 2, 4, 8.



Constraints:
1 <= n <= 1000
"""
# Time: O(√n + k log k) Space: O(k)
class Solution:
    def divisors(self, n):
        result = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                result.append(i)
                if i != n // i:
                    result.append(n//i)
            i += 1
        result.sort()
        return result