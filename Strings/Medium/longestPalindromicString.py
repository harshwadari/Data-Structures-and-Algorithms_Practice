# 5. Longest Palindromic Substring

# buret approach using two pointer nested loops
# TC = O(N^3) and SC = O(1)
def LongestPalindrome(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i,n):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                if len(sub) > len(longest):
                    longest = sub
    return longest