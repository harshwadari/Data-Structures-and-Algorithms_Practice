# 1189. Maximum Number of Balloons
"""
Given a string text, you want to use the characters of 
text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return 
the maximum number of instances that can be formed.
"""

# Optimal solution using hashing
# TC = O(N) and SC = O(26) = ( ignoring constant) O(1)
def balloons(text:str) -> int:
    freq = {}
    for i in range(len(text)):
            if text[i] in freq:
                freq[text[i]] += 1
            else:
                freq[text[i]] = 1
    return min(
        freq.get('b',0),
        freq.get('a',0),
        freq.get('l',0) // 2,
        freq.get('o',0) // 2,
        freq.get('n',0)
    )