# Valid Palindrome gfg format 

# iterative Approach

# TC = O(1/2 * N) = O(N) and SC = O(1)
def isPalindrome(s: list[str]) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Recursive Appraoch
# TC = O(1/2 * N) = O(N) and SC = O(N/2) stack space 

def ispalindrome(s):
    def func(s,left,right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return func(s,left + 1, right - 1)