# Basics of Bit Manipulation 

# Understand binary to decimal conversion and vice versa 
# TC O(log n)  and SC = O(log n) 
def decimal_to_binary(n):
    binary = ''
    while n != 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
print(decimal_to_binary(13))




# TC = O(log n) and SC = O(log n)
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
print(binary_to_decimal('1101'))



# bitwise AND operator in python  (& works at the binary (bit) level, not logical level.)
#TC = O(1) and SC = O(1)
def bitwiseAND(a, b):
    return a & b
print(bitwiseAND(13, 7))  


# bitwise OR operator in python (| works at the binary (bit) level, not logical level.)
#TC = O(1) and SC = O(1)
def bitwiseOR(a,b):
    return a | b
print(bitwiseOR(13, 7))

# bitwise XOR operator in python (^ works at the binary (bit) level, not logical level.)
# TC = O(1) and SC = O(1)
# bitwise xor means that if the number of ones are even then the result is 0 
# and if the number of ones are odd then the result is 1

def bitwiseXOR(a,b):
    return a ^ b
print(bitwiseXOR(13, 7))


# shift operators in python (>> and << works at the binary (bit) level, not logical level.)

# right shift operator (>> shifts the bits to the right and fills the leftmost bits with 0)
#TC = O(1) and SC = O(1)

# formula of right shift is a >> n = a // (2 ** n)
def rightShift(a, n):
    return a >> n
print(rightShift(13, 2))  

# right shift operator (<< shifts the bits to the left and fills the rightmost bits with 0)
# TC = O(1) and SC = O(1)
# formula of left shift is a << n = a * (2 ** n)
def leftShift(a, n):
    return a << n
print(leftShift(13, 2))


# Not operator in python (~ works at the binary (bit) level, not logical level.)
# TC = O(1) and SC = O(1)
def bitwiseNOT(a):
    return ~a
print(bitwiseNOT(13))