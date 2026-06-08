# Find Nth root of a number

# brute appraoch using built in function
# TC = O(1) and SC = O(1)

def nthroot(n:int,m:int)-> int:
    result = round(m ** (1/n))
    if result ** n == m:
        return result
    return -1


# Optimal Approach using binary search on answer space
# TC = O(NlogN) and SC = O(1)
def rootbsnth(n,m):
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        if mid ** n == m:
            return mid
        elif mid ** n <  m:
            low = mid + 1
        else:
            high = mid - 1
    return -1