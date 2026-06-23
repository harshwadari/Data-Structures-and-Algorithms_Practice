# GFG potd 23 june 2026
"""
There are infinitely many people standing in a row, indexed from 1. 
The strength of the person at index i is i².

Given a strength p, determine the maximum number of people that can be 
defeated. A person with strength x can be defeated only if p ≥ x, after 
which the strength p decreases by x.

Examples :

Input: p = 14
Output: 3
Explanation: The strengths of the first few people are 1, 4, 9, 16, ....
Defeating the first three people consumes 1 + 4 + 9 = 14 strength, leaving 0. 
Therefore, the maximum number of people that can be defeated is 3.
"""

# Better approach by checking all conditions
# TC = O(p ^ 1/3) and SC = O(1)
def people(p: int) -> int:
    defeated = 0
    i = 1
    while i * i <= p:
        defeated += 1
        p -= i * i
        i += 1
    return defeated

# Optimal appraoch using math formula and binary seach
# TC = O(logN) where n is power and SC = O(1)
def defeat(p:int) -> int:
    defeated = 0
    low = 0
    high = p
    while low <= high:
        mid = (low + high) // 2
        strength_needed = mid * (mid + 1) * (2 * mid + 1) // 2
        if strength_needed <= p:
            defeated = mid
            low = mid + 1
        else:
            high = mid - 1
    return defeated 