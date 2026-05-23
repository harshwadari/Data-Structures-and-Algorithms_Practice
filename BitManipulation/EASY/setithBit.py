# set ith bit of a number

# brute force approach is to convert the number to binary 
# and set the ith bit to 1 and then convert it back to decimal

# TC = O(log n) and SC = O(log n)
def set_ith_bit(n, i):
    binary = ""
    while n != 0:
        binary = str(n % 2) + binary
        n = n // 2
    if i < len(binary):
        binary = binary[:-i-1] + '1' + binary[-i:]
    else:
        binary = '1' + '0' * (i - len(binary)) + binary
    return int(binary, 2)

# optimal approach is to use bitwise OR operator
# TC = O(1) and SC = O(1)
def set_ith_bit_optimal(n, i):
    return n | (1 << i)