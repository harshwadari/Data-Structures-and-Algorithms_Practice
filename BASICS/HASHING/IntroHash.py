"""

Hashing in Python — Straight to the Point
 What is Hashing?

Hashing is a technique to store and retrieve data in O(1) time (average) using a hash function.

It converts a key into an index where the value is stored.

In Python, hashing is mainly used in:

dict {}  dict can store duplicate values but not duplicate keys. It is an unordered collection of key-value pairs. It is mutable and indexed by keys.

set () set is an unordered collection of unique elements. It is mutable and does not allow duplicate values.
"""


# Hashing template code using dictionary
# TC = O(N) and SC = O(N)
def hashingdict(nums):
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq: # in here is called membership operator which checks if the element is present in the dictionary or not
            freq[nums[i]] +=1
        else:
            freq[nums[i]] =1
    # for key , value in freq.items():
    #   return freq[nums[i]][key,value]

    return freq
print(hashingdict([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]))
