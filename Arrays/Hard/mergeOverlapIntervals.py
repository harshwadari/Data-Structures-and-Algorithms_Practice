# Merge overlaping Intervlas LC 56

"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""


# brute approach 

# TC = O(N^2) and SC = O(N)
def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        n = len(intervals)
        for i in range(n):
            if intervals[i] == None:
                continue
            for j in range(i+1,n):
                if intervals[j] == None:
                    continue
                s1,e1 = intervals[i]
                s2,e2 = intervals[j]
                if s2 <= e1:
                    intervals[i] = [min(s1,s2) , max(e1,e2)]
                    intervals[j] = None
        result = []
        for x in intervals:
            if x:
                result.append(x)
        return result

"""
Better Approach
Idea

Sort intervals by start

For each interval check with last merged interval

Instead of checking with all previous intervals, check only the last one.

Key Insight

After sorting:

if current.start <= last.end
    merge
else
    add new interval
"""


# code 
# TC = O(NlogN) and SC = O(N)
def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = []
        n = len(intervals)
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
      

#optimal one 

class Solution:
    def merge(self, intervals):
        intervals.sort()

        merged = []
        for start, end in intervals:

            if not merged or merged[-1][1] < start:
                merged.append([start,end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged