# 2144. Minimum Cost of Buying Candies With Discount

"""
Optimal approach using sorting and greedy approach
TC = O(NlogN) and SC = O(1)
"""
def minimumCost(cost: list[int]) -> int:
    cost.sort()
    result = 0
    count = 1
    for i in range(len(cost)-1,-1,-1):
        if count != 3:
            result += cost[i]
            count += 1
        else:
            count = 1
    return result