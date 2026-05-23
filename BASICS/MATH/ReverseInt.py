# Reverse Integer

"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


# pythonic way 

def revint(n:int):
    sign = -1 if n < 0 else 1
    rev = int(str(abs(n))[::-1]) * sign
    if rev < -2 ** 31 or rev > 2 ** 31 - 1:
        return 0
    return rev
print(revint(4))


# otpimal approach using math logic

def reverseInt(n : int):
    if n < 0:
        sign = -1
    else:
        sign = 1
    n = abs(n)
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    rev *= sign
    if rev < -2 ** 31 or rev > 2 ** 31:
        return 0
    return rev
print(reverseInt(-893))