# 191. Number of 1 Bits

# extreme naive brut apparoch
# TC = O(logn^2) and SC = O(logN)
def countsetbit(n):
    binary = []
    while n > 0:
        if n % 2 == 0:
            binary.append('0')
        else:
            binary.append('1')
        n = n // 2
    count = 0
    for i in range(binary):
        if binary[i] == '1':
            count += 1
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