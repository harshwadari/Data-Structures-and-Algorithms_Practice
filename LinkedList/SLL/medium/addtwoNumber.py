# Add two numbers in linked list
# brut force approach
"""
Brute Force Approach
Idea

Convert both linked lists → integers.

Add the integers.

Convert result back → linked list.

Steps
LL1 → number
LL2 → number
sum = num1 + num2
convert sum → linked list
"""



"""
Better Approach (Simulating Addition)
Idea

Add digits like we do in school addition.

2 -> 4 -> 3
5 -> 6 -> 4
------------
7 -> 0 -> 8

Use carry.

Algorithm

While:

l1 exists
OR
l2 exists
OR
carry exists

Compute:

sum = val1 + val2 + carry
digit = sum % 10
carry = sum // 10

Add digit to result list.
"""
