# 8. String to Integer (atoi)
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', 
assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character 
is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], t
hen round the integer to remain in the range. Specifically, integers less than -231 
should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
"""
# Optimal appraoch using iterative solution 
# String to integer (atoi)


# optimal appoach 
# TC = O(2N) and SC = O(1)
def atoi(s):
    i = 0
    n = len(s)
    while i < n and s[i] == " ":
        i +=1
    sign = 1
    if i < n and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i +=1  
    num = 0
    int_max = 2**31 -1
    int_min = -2**31
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord("0")
        if num > int_max//10 or (num == int_max//10 and s[i] > "7"):
            return int_max if sign == 1 else int_min
        num = num * 10 + digit
        i +=1
    return sign * num



# Recursive approach 
# TC = O(N) and SC = O(N)
def atoi(s):
    i = 0
    n = len(s)

    # Skip leading spaces
    while i < n and s[i] == " ":
        i += 1

    # Determine sign
    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    def solve(index, num):
        # Base case
        if index >= n or not s[index].isdigit():
            return num

        digit = ord(s[index]) - ord('0')

        # Overflow check
        if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else -INT_MIN

        return solve(index + 1, num * 10 + digit)

    ans = solve(i, 0)
    ans *= sign

    if ans > INT_MAX:
        return INT_MAX
    if ans < INT_MIN:
        return INT_MIN

    return ans