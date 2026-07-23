# 1071. Greatest Common Divisor of Strings
"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t
 + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both s
tr1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""​​​​​​​

 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

# Optiamal Appraoch using calculating gcd by using eucledian Algorithm
# TC = O(min(log(a,b))) and SC = O(N)
def gcdStrings(str1:list[str],str2:list[str]) -> int:
    if str1 + str2 != str2 + str1:
        return ""
    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    m = len(str1)
    n = len(str2)
    length = gcd(m,n)
    return str1[:length]
