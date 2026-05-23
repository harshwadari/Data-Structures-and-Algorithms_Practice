"""

Hashing in Python — Straight to the Point
 What is Hashing?

Hashing is a technique to store and retrieve data in O(1) time (average) using a hash function.

It converts a key into an index where the value is stored.

In Python, hashing is mainly used in:

dict {}

set ()
"""


# Hashing template code using dictionary
# TC = O(N) and SC = O(N)
def hashingdict(nums):
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] +=1
        else:
            freq[nums[i]] =1
    # for key , value in freq.items():
    #   return freq[nums[i]][key,value]

    return freq
print(hashingdict([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]))
