# 901. Online Stock Span

# Brute solution 
"""
But this will TLE

Time Complexity:

O(n) per next()

For n calls:

O(n²)
"""
class StockSpanner(object):

    def __init__(self):
        self.arr = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.arr.append(price)
        count = 1
        for i in range(len(self.arr)-2,-1,-1):
            if self.arr[i] <= price:
                count += 1
            else:
                break
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)