# Divide Two Integers without using multiplication, division and mod operator
# brute force approach is to keep subtracting the divisor from the dividend until the dividend is less than the divisor
# TC = O(N) and SC = O(1)
def divide(dividend, divisor):
    if divisor == 0:
        return float('inf')  # Handle division by zero case
    if dividend == 0:
        return 0
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return sign * quotient


# optimal approach using bit manipulation
# TC = O(log N) and SC = O(1)
def divide_bit(dividend, divisor):
    if divisor == 0:
        return float('inf')  # Handle division by zero case
    if dividend == 0:
        return 0
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    for i in range(31, -1, -1):
        if (dividend >> i) >= divisor:
            dividend -= divisor << i
            quotient += 1 << i
    return sign * quotient