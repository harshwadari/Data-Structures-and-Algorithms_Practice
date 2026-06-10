# Fractional Knapsack

# optimal approach using greedy algorithm
# TC = O(NlogN) and SC = O(1)
def fractionalKnapsack(self, val, wt, capacity):
        #code here
        items = []
        for i in range(len(val)):
            items.append((val[i] / wt[i] , val[i] , wt[i]))
        items.sort(reverse=True)
        total_value  = 0.0
        for ratio, value, weight in items:
            if capacity >= weight:
                total_value += value
                capacity -= weight
            else:
                total_value += ratio * capacity
                break
        return total_value