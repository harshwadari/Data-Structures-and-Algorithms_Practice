# Print Divisor of any number
"""
A divisor of any number is the number that completely divides that number
"""
# TC = O(N) and SC = O(N)
def divisor(n:int):
    result = []
    for i in range(1,n):
        if n % i == 0:
            result.append(i)
    return result
print(divisor(36))


# optimal approach 
#  TC = O(sqrt(n)) and SC = O(N)
def divisors(self, n):
    result = []  
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)  
            if i != n // i:
                result.append(n // i)
    return sorted(result)