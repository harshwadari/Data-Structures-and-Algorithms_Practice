# Divisibility check of any number 
"""
Your give any interger n and a string and you have to check that interger is
divisible by given string
example:
input : n = 8 , string = 48
ouput : True
constraints:
1 <= n <= 10 ^ 5
len(string) <= 10 ^ 5

"""
# TC = O(N) and SC = O(1)
def divisibility(n:int,s:str) -> bool:
    remainder = 0
    for char in s:
        remainder = (remainder * 10 + int(char)) % n
    if remainder == 0:
        return True
    return False