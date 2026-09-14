# 739. Daily Temperatures
"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have 
o wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


# Brute Force Appraoch 
# TC = O(n ^ 2) and SC = O(N)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j]  > temperatures[i]:
                    result[i] = j - i
                    break
        return result

# Optimal Appraoch using Monotonic stack 
# TC = O(N) and SC = O(N
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1] - i
            stack.append(i)
        return result