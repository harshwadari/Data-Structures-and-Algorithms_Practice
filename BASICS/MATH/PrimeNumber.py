# To check given Number is prime or not 
# TC = O(N) and SC = O(1)
def isPrime(n:int):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    return True
print(isPrime(47))


# To count all Prime numbers 