# 1838. Frequency of the Most Frequent Element


"""
The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an 
index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
"""


# brute force 
"""
Sort → ensures left side usable
Fix target → nums[i]
Go backward → pick cheapest elements first
Start count = 1 → target itself
Track max → answer
"""

# TC = O(N^2) and SC = O(1)
def maxfreq(nums,k):
    n = len(nums)
    nums.sort()
    maxfreq = 1
    for i in range(n):
        target = nums[i]
        count = 1
        cost = 0
        for j in range(i - 1 , - 1, - 1):
            cost += target - nums[j]
            if cost > k:
                break
            count +=1
        maxfreq = max(maxfreq, count)
    return maxfreq



# optimal approach using sliding window
# TC = O(n log n) + O(n) = O(n log n) and SC = O(1)

def maxifreq(nums,k):
    nums.sort()
    left = 0
    total = 0
    maxfreq = 1
    for right in range(len(nums)):
        total += nums[right]
        while nums[right] * (right - left + 1) - total > k:
            total -= nums[left]
            left +=1
        maxfreq = max(maxfreq,right - left + 1)
    return maxfreq