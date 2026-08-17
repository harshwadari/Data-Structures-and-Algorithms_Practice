"""
Given a String s and integer k . find the length of the longest substring in which at most k
distinct characters have an odd frequency 
A character  has an odd frequency if it  appears an odd numbers of times in the substring 


Example 1 :
input:
s = "aabbcde"
k = 2

output:
6
explanation:
The longest substring is "aabbcd"
it's char freq are :
a -> 2 (even)
b -> 2 (even)
c -> 1 (odd)
d -> 1 (odd)
There are 2 chars with odd freq which is allowed because k = 2


Example 2 :
Input:
s = "abcba"
k = 1

output:
5


explanation:
The entire String is "abcba" is valid :
a -> 2 (even)
b -> 2 (even)
c -> 1 (odd)

only 1 char has an odd freq so the answer is 5

constrainst:
1 <= s.lenght <= 10 ^ 5
0 <= k <= 26
s conatains only lowercase english characters
"""

# Optimal Appraoch using sliding window and hashmap


# TC = O(2N) ~ O(N) and SC = O(26) ~ O(1)

def atmostoddfreq(s:str,k:int) -> int:
    left = 0
    freq  = {}
    maxlen = 0
    oddcount = 0
    for right in range(len(s)):
        char = s[right]
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
        if freq[char] % 2 == 1:
            oddcount += 1
        else:
            oddcount -= 1
        while oddcount > k:
            char = s[left]
            freq[char] -= 1
            if freq[char] % 2 == 1:
                oddcount += 1
            else:
                oddcount -= 1
            left += 1
        maxlen = max(maxlen,right - left + 1) 
    return maxlen 
def main():
    t = int(input())

    for _ in range(t):
        s = input().strip()
        k = int(input())

        print(atmostoddfreq(s, k))


if __name__ == "__main__":
    main()