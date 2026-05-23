# Armstrong Number
"""
A number is armstrong when it's digit is same when it is taken cube sum of all digits
"""
# TC = O(logN) and SC = O(1)
def armstrongnum(n:int):
    if n < 0:
        return False
    original = n
    sum = 0
    while n != 0:
        digit = n % 10 
        sum += digit  ** 3
        n = n // 10
    if sum == original:
        return True
    else:
        return False
print(armstrongnum(153))