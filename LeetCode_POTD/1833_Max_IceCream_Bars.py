# 1833. Maximum Ice Cream Bars
"""
Constraints:

costs.length == n
1 <= n <= 105
1 <= costs[i] <= 105
1 <= coins <= 108
"""

# optimal solution using greedy appraoch and sorting
# TC = O(NlogN) and SC = O(1)

def iceCreamBars(costs: list[int] , coins: int) -> int:
    costs.sort()
    max_Icecream_bars = 0
    for i in range(len(costs)):
        if costs[i] <= coins:
            max_Icecream_bars += 1
            coins -= costs[i]
    return max_Icecream_bars


# More Optimal solution using counting sort 
# TC = O(N + 10 ^5) and SC = O(1)
def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        freq = [0] * 100001

        for cost in costs:
            freq[cost] += 1

        ans = 0

        for cost in range(1, 100001):
            if freq[cost] == 0:
                continue

            can_buy = min(freq[cost], coins // cost)

            ans += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return ans