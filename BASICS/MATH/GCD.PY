# GCD/ HCF of  a given two number 





"""
==========================
GCD & LCM CHEAT SHEET
==========================

1. Sum of first n natural numbers
   = n * (n + 1) // 2

2. Sum of first n even numbers
   = n * (n + 1)

3. Sum of first n odd numbers
   = n * n

--------------------------------------------------

Greatest Common Divisor (GCD)

Definition:
Largest number that divides both a and b.

Euclidean Algorithm:
while b != 0:
    a, b = b, a % b
return a

Formula:
gcd(a, b) = gcd(b, a % b)

Time Complexity:
O(log(min(a, b)))

--------------------------------------------------

Least Common Multiple (LCM)

Definition:
Smallest positive number divisible by both a and b.

Formula:
lcm(a, b) = (a * b) // gcd(a, b)

Relationship:
gcd(a, b) * lcm(a, b) = a * b

--------------------------------------------------

Properties

1. gcd(a, a) = a

2. gcd(a, 0) = a

3. gcd(0, a) = a

4. lcm(a, a) = a

5. lcm(a, 0) = 0

6. gcd(a, b) = gcd(b, a)

7. lcm(a, b) = lcm(b, a)

8. gcd(a, b) <= min(a, b)

9. lcm(a, b) >= max(a, b)

10. Consecutive numbers:
    gcd(n, n + 1) = 1

11. If gcd(a, b) = 1,
    then a and b are Coprime.

12. gcd(a * x, a * y)
    = a * gcd(x, y)

13. lcm(a * x, a * y)
    = a * lcm(x, y)

--------------------------------------------------

GCD of an Array

g = arr[0]
for i in range(1, len(arr)):
    g = gcd(g, arr[i])

Time:
O(n log M)

where M = maximum element.

--------------------------------------------------

LCM of an Array

l = arr[0]
for i in range(1, len(arr)):
    l = (l * arr[i]) // gcd(l, arr[i])

Time:
O(n log M)

--------------------------------------------------

Useful Observations

gcd(n², n(n+1))
= n × gcd(n, n+1)
= n

LCM(a, b)
= (a * b) // gcd(a, b)

Product Formula
gcd × lcm = product of numbers

--------------------------------------------------

Python GCD Function

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

Python LCM Function

def lcm(a, b):
    return (a * b) // gcd(a, b)

==========================

"""
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
    while n2 != 0:
        n1,n2 = n2,n1 % n2
    return n1

print(gcdoptimal(12, 45))  # 3



# To Caculate gdc in array 

class Solution:
    def gcd1(self,a,b):
        while b != 0:
            a,b = b, a % b
        return a
    def gcd(self, n, arr):
        # code here 
        g = arr[0]
        for i in range(1,len(arr)):
            g = self.gcd1(g,arr[i])
        return g
    

# GCD and LCM 

class Solution:
    def lcmAndGcd(self, a: int, b: int):
        x = a
        y = b

        while b != 0:
            a, b = b, a % b

        gcd = a
        lcm = (x * y) // gcd

        return [lcm, gcd]