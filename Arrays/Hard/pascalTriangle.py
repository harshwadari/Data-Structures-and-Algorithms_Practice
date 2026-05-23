"""
Instead use the relation:




So we build each row from the previous value in O(1) time.

Time Complexity

O(n²)

Space Complexity

O(1) (if just printing)

“In Pascal’s Triangle each element is a binomial coefficient C(n, r). 
Instead of computing factorials repeatedly, we use the relation
C(n,r+1) = C(n,r) × (n−r)/(r+1) to generate the next value in constant 
time. This lets us build each row efficiently in O(n²).”
"""


def pascal_triangle(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

pascal_triangle(10)