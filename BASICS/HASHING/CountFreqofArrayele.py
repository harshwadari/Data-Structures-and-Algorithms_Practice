"""
Given an array nums of size n which may contain duplicate elements.
Rreturn a list of pairs where each pair contains a unique element 
from the array and its frequency in the array.
You may return the result in any order, but each element must appear exactly once in the output.

Example 1

Input: nums = [1, 2, 2, 1, 3]

Output: [[1, 2], [2, 2], [3, 1]]

Explanation:

- 1 appears 2 times

- 2 appears 2 times

- 3 appears 1 time

Order of output can vary.
"""

# optimal solution 
# TC = O(N) and SC = O(N)
def countfreq(nums:list[int]) ->list[int]:
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    result = []
    for key , value in freq.items():
        result.append((key,value))
    return result,freq
print(countfreq([5,3,7,8,8,8,9,1]))

# return most/ highest occuring element in array
# TC = O(N) and SC = O(N)
def mostFreqEle(arr:list[int])->int:
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    max_freq = 0
    ans = -1
    for num in freq:
        if freq[num] > max_freq:
            max_freq = freq[num]
            ans = num
        elif freq[num] == max_freq:
            ans = max(num,ans)
    return ans