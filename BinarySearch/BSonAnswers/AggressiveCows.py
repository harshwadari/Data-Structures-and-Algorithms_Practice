# Aggressive cows

"""
https://practice.geeksforgeeks.org/problems/aggressive-cows/1
"""

# Optimal solution using Binary Search on answers

"""
Time Complexity (TC)
Break it down:
Sorting stalls → O(n log n)
Binary search range → from 1 to (max - min)
→ takes O(log D) where D = stalls[-1] - stalls[0]
ispossible() check → O(n) each time

👉 Total:
O(nlog⁡n+nlog⁡D)O(n \log n + n \log D)O(nlogn+nlogD)

SC = O(1)
"""


def cows(stalls,k):
    stalls.sort()
    ans = 0
    left = 1
    right = (len(stalls) - 1) - stalls[0]
    while left <= right:
        mid = (left + right) // 2
        if isPossible(stalls,mid,k):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
def isPossible(stalls,k,maxsum):
    count = 1
    lastPos = stalls[0]
    for i in range(1,len(stalls)):
        if stalls[i] - lastPos >= maxsum:
            count += 1
            lastPos = stalls[i]
        if count == k:
            return True
    return False