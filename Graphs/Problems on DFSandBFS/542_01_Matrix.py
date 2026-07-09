# 542. 01 Matrix
"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 
"""
from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        distance = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    distance[i][j] = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while len(queue) != 0:
            row,col = queue.popleft()
            for dr ,dc in directions:
                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and distance[new_row][new_col] == -1):
                    distance[new_row][new_col] = distance[row][col] + 1
                    queue.append((new_row,new_col))
        return distance