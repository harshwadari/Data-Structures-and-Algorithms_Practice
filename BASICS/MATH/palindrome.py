# . Palindrome Number

# optimal solution using reversing number
# TC = O(logN) and SC = O(1)
def palindrome(n:int):
    if n < 0:
        return False
    original = n
    reverse = 0
    while n != 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if original == reverse:
        return True
    return False