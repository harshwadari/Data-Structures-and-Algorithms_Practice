
# brute appraoch

# TC = O(N) and SC = O(N)
class MinStack(object):

    def __init__(self):
        self.x = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.x.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.x) == 0:
            return None
        return self.x.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.x) == 0:
            return None
        return self.x[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.x)
        



# Optimal appraoch 


