# 2094. Finding 3-Digit Even Numbers
"""
You are given an integer array digits, where each element is a digit. The array 
may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

 

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.
 

Constraints:

3 <= digits.length <= 100
0 <= digits[i] <= 9
"""

# better appraoch using three nested loops and using set and sorting 
# TC = O(NlogN + N ^ 3) and SC = O(N)
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        n = len(digits)
        ans = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(num)
        return sorted(list(ans))



# Optimal Appraoch using hashmap
"""
Build frequency: O(n)
Generate numbers: O(10 × 10 × 5) = O(1)

Total: O(n)
Space: O(1)
"""
class Solution(object):
    def findEvenNumbers(self, digits):
        freq = [0] * 10

        for digit in digits:
            freq[digit] += 1

        ans = []

        for i in range(1, 10):          # hundreds digit
            if freq[i] == 0:
                continue

            freq[i] -= 1

            for j in range(10):         # tens digit
                if freq[j] == 0:
                    continue

                freq[j] -= 1

                for k in range(0, 10, 2):   # units digit
                    if freq[k] > 0:
                        num = i * 100 + j * 10 + k
                        ans.append(num)

                freq[j] += 1

            freq[i] += 1

        return ans