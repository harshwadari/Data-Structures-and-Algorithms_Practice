# 1091. Shortest Path in Binary Matrix
"""
Given an n x n binary matrix grid, return the length of the shortest clear path 
in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to 
the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are 
different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
"""
from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
        if rows == 1 and cols == 1:
            return 1
        queue = deque()
        queue.append([1,0,0])
        grid[0][0] = 1
        while len(queue) != 0:
            dist,i,j = queue.popleft()
            directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
            for x ,y in directions:
                newI = x + i
                newJ = y + j
                if newI < 0 or newJ < 0 or newI >= rows or newJ >= cols:
                    continue
                if grid[newI][newJ] == 1:
                    continue
                if newI == rows - 1 and newJ == cols - 1:
                    return dist + 1
                grid[newI][newJ] = 1
                queue.append([dist + 1,newI,newJ])
        return -1