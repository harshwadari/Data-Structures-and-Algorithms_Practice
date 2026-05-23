# Check if the ith bit is set or not 

# brute force approach is to convert the number to binary and check if the ith bit is 1 or not
# TC = O(log n) and SC = O(log n)
def check_ith_bit(n, i):
    binary = ""
    while n != 0:
        binary = str(n % 2) + binary
        n = n // 2
    if i < len(binary) and binary[-i-1] == '1':
        return True
    return False

# optimal approach is to use bitwise AND operator
# TC = O(1) and SC = O(1)
def check_ith_bit(n, i):
    if (n & (1 << i)) != 0:
        return True
    return False


# optimal approach using right shift operator
# TC = O(1) and SC = O(1)
def checkitbitright(n,i):
    if n & (n >> i) == 1 :
        return True
    return False

