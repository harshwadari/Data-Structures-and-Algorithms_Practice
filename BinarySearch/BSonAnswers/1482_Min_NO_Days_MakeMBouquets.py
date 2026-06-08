# 1482. Minimum Number of Days to Make m Bouquets

"""
Docstring for BinarySearch.BSonAnswers.3
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent
flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] 
and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to 
make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Example 2:

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers
. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1


Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
"""


# burte force method 
# TC = O(F* D) where f is no of flowers and d is maxday - minday+1
# SC = (1)
def bloomiday(nums,m,k):
    n = len(nums)
    if m*k >n:
        return -1
    min_day = nums[0]
    max_day = nums[0]
    for i in range(n):
        if nums[i] < min_day:
            min_day = nums[i]
        if nums[i] > max_day:
            max_day = nums[i]
    day = min_day
    while day <= max_day:
        bouquets = 0
        flowers = 0
        i = 0
        while i < n:
            if nums[i] <= day:
                flowers +=1
                if flowers == k:
                    bouquets +=1
                    flowers =0
            else:
                flowers = 0
            i +=1
        if bouquets >= m:
            return day
        day +=1
    return -1
print(bloomiday([1,10,3,10,2],3,1))


