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
    

# Leetcode approach for valid plaindrome with spaces comma

def validpalindrome(s:str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True
print(validpalindrome( "A man, a plan, a canal: Panama"))