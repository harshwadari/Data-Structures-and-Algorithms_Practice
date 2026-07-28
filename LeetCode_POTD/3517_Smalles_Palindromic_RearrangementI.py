# 3517. Smallest Palindromic Rearrangement I
"""
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

 

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.
"""

"""
"Python strings are immutable, so repeated += may create new strings repeatedly. 
Using a list and ''.join() constructs the final string in one pass and is the recommended approach. 
In this specific problem, += is still effectively O(n) because there are at most 26 distinct lowercase 
letters, but join() is the more scalable and idiomatic solution."
"""
# Optimal Approach using sorting and hash mapping 
"""
| Operation           | Time                  | Space           |
| ------------------- | --------------------- | --------------- |
| Count frequency     | `O(n)`                | `O(1)`          |
| Sort distinct chars | `O(k log k)` → `O(1)` | `O(k)` → `O(1)` |
| Build left half     | `O(n)`                | `O(n)`          |
| `join()`            | `O(n)`                | `O(n)`          |
| Reverse             | `O(n)`                | `O(n)`          |
| Final concatenation | `O(n)`                | `O(n)`          |
| **Overall**         | **`O(n)`**            | **`O(n)`**      |

"""
def palindrome(s:str) -> str:
    if len(s) == 1:
        return s
    freq = {}
    for i in range(len(s)): #O(N)
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]]  = 1
    left = []
    middle = ""
    for char in sorted(freq.keys()): # O(K logK)
        left.append(char * (freq[char]//2))
        if freq[char] % 2 == 1:
            middle = char
    left = "".join(left)
    return left + middle + left[::-1]
    