#451. Sort Characters By Frequency
"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""

# better approach using dictionary and sroting
# TC = O(N log N) and SC = O(N)
def sortcharfreq(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for char, count in sorted_freq:
        result += char * count
    return result
   
# optimal approach using bucket sort
# TC = O(N) and SC = O(N)
def sortcharfreqoptimal(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    buckets = [[] for _ in range(len(s) + 1)]
    for char, count in freq.items():
        buckets[count].append(char)
    result = ""
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            result += char * i
    return result
