# Count the number of set Bits

# extreme naive brut apparoch
# TC = O(logn^2) and SC = O(logN)
def countsetbit(n):
    binary = ''
    count = 0
    while n != 0:
        binary = str(n % 2) + binary
        n = n //2
    for val in binary:
        if val == '1':
            count +=1
    return count

# better brute approach
# TC = O(logN) and SC = O(1)
def countsetbitb(n):
    count = 0
    while n != 0:
        if n % 2 == 1:
            count +=1
        n = n //2
    return count


# optimal appraoch 
# TC = O(1) and SC = O(1)

def countset(n):
    count = 0
    while n :
        n = n & (n - 1)
        count +=1
    return count