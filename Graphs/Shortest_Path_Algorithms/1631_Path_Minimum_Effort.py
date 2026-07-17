# 1631. Path With Minimum Effort
"""
You are a hiker preparing for an upcoming hike. You are given heights, 
a 2D array of size rows x columns, where heights[row][col] represents 
the height of cell (row, col). You are situated in the top-left cell, 
(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) 
(i.e., 0-indexed). You can move up, down, left, or right, and you wish to find 
a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two 
consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.



Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

# Optimal Appraoch using Dijkstra's  Algorithm

import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])
        effort = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        effort[0][0] = 0
        queue = [[0,0,0]]
        while len(queue) != 0:
            eff ,i ,j = heapq.heappop(queue)
            if i == rows - 1 and j == cols - 1:
                return eff
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for x , y in directions:
                newI = x + i
                newJ = y + j
                if newI < 0 or newJ < 0 or newI >= rows or newJ >= cols:
                    continue
                neweff = max(eff,abs(heights[newI][newJ]- heights[i][j]))
                if neweff < effort[newI][newJ]:
                    effort[newI][newJ] = neweff
                    heapq.heappush(queue,[neweff,newI,newJ])