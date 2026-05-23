# koko eating bananas

"""
Docstring for BinarySearch.BSonAnswers.1
Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. The guards have gone 
and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead 
and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating
all the bananas before the guards return.
Return the minimum integer k such that she can eat all
the bananas within h hours.

 
Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
"""

# brute force approach 
# TC + O(maxPiles *N) and SC  = O(1)
def koko(piles,h):
    n = len(piles)
    maxPiles = max(piles)
    for i in range(1,maxPiles+1):
        hours = 0
        for pile in piles:
            hours += (pile+i-1)//i
        if hours <= h:
            return i
print(koko([3,6,7,11],8))
        

# optimal appraoch using binary search
# TC = O(logN) and SC = O(1)
def bskoko(piles,h):
    low = 1
    high = max(piles)
    ans = high
    while low <= high:
        mid = (low+high)//2
        hours = 0
        for i in range(len(piles)):
            hours += (piles[i] + mid-1)//mid
        if hours <=h:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
print(bskoko([3,6,7,11],8))