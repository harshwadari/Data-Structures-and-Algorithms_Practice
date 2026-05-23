# GCD/ HCF of  a given two number 
# TC = O(min(n1,n2)) and SC = O(1)
def gcdnum(n1,n2):
    gcd = 1
    for i in range(1,min(n1,n2)):
        if (n1 % i == 0) and (n2 % i == 0):
            gcd = i
            break
    return gcd


# optimal approach using eculidean algorithm
# TC = O(logN) and SC = O(1)
"""
Euclidean Algorithm states that 
gcd(a,b) = gcd(a-b,b) where a > b
derived logic from this gcd(a,b) = gcd(a % b ,b) where a > b
"""

def gcdoptimal(n1: int, n2: int):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    
    if n1 == 0:
        return n2
    else:
        return n1

print(gcdoptimal(12, 45))  # 3