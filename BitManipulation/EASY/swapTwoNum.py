# Swap two numbers without using a temporary variable

# brute force approach 
# TC = O(1) and SC = O(1)
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# optimal approach using bit manipulation
# TC = O(1) and SC = O(1)
def swapbit(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b