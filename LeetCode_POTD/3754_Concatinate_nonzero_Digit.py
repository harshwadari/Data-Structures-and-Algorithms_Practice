# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
"""
You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.

 

Example 1:

Input: n = 10203004

Output: 12340

Explanation:

The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
Therefore, the answer is x * sum = 1234 * 10 = 12340.

"""

# convertin string appraoch 
# Time Complexity: O(log n) Space Complexity: O(log n)
def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        x = []
        sum = 0
        for c in str(n):
            if c != '0':
                x.append(c)
                sum += int(c)
        return int(("".join(x))) * sum

# Optimal appraoch using arithmetic
# Time: O(d) where d is the number of digits. Space: O(1). 
class Solution(object):
    def sumAndMultiply(self, num):
        result = 0
        place = 1
        digit_sum = 0

        while num > 0:
            digit = num % 10

            if digit != 0:
                result += digit * place
                digit_sum += digit
                place *= 10

            num //= 10

        return result * digit_sum