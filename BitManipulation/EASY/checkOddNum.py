# Check if given number is odd or not
# TC = O(1) and SC = O(1)
def checkodd(n):
    if n % 2 != 0:
        return True
    return False

# optimal approach using bit manipulation
# TC = O(1) and SC = O(1)
def checkoddbit(n):
    if n & 1 == 1:
        return True
    return False