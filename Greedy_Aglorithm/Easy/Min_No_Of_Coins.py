# Minimum number of Coins

'''
Given an infinite supply of each denomination of 
Indian currency { 1, 2, 5, 10 } and a target value n. 
Find the minimum number of coins and/or notes needed to make the change for Rs n. 

Examples:

Input: n = 39
Output: 6
Explaination: 39 can be formed using 3 coins of 10 rupees, 
1 coin of 5 rupees and 2 coins of 2 rupees so minimum coins required are 6.
'''
# TC = O(N) and SC = O(1)
def MinCoins(n:int) -> int:
    coins = [10,5,2,1]
    coinsUsed = 0
    for coins in coins:
        coinsUsed += n / coins
        n %= 10
    return coinsUsed