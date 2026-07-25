# 3536. Maximum Product of Two Digits
"""
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.
Example 2:

Input: n = 22

Output: 4

Explanation:

The digits of n are [2, 2].
The possible products of any two digits are: 2 * 2 = 4.
The maximum product is 4.
Example 3:

Input: n = 124

Output: 8

Explanation:

The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.
 

Constraints:

10 <= n <= 109
 

"""
# Naive Approach using sorting
# TC = O(nlogd) and SC = O(d) where d is digits
def product(n):
    result = []
    while n != 0:
        digits = n % 10
        n = n //10
        result.append(digits)
    result.sort()
    return result[-1] * result[-2]


# Better approach using 
# TC = O(d) and SC = O(1)
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = -1
        second = -1
        while n != 0:
            digit = n % 10
            if digit >= first:
                second = first
                first = digit
            elif digit > second:
                second = digit
            n = n // 10
        return first * second


# different Appraoch 
def maxiproduct(n:int) -> int:
    x = sorted(str(n))
    return int(x[-1]) * int(x[-2])