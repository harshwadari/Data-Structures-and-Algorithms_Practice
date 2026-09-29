# set ith bit of a number

# brute force approach is to convert the number to binary 
# and set the ith bit to 1 and then convert it back to decimal

# TC = O(log n) and SC = O(log n)
def set_ith_bit(n, i):
    binary = []
    while n > 0:
        if n % 2 == 0:
            binary.append('0')
        else:
            binary.append('1')
        n = n // 2
    binary.reverse()
    binary[i] = '1'
    return "".join(binary)
print(set_ith_bit(34,2))







# optimal approach is to use bitwise OR operator
# TC = O(1) and SC = O(1)
def set_ith_bit_optimal(n, i):

    return n | (1 << i)





# Clear ith Bit
# TC = O(1) and SC = O(1)
def clearkthbit(n,k):
    return n & ~(1 << k)





# Toggle the ith bit 
# TC = O(1) and SC = O(1)
def toggle(n,k):
    return n ^ (1 << k)



