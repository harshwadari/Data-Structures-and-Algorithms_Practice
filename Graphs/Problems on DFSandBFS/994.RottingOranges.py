# 994. Rotting Oranges

# Brute Force Approach 

# Time = O((m*n)²) and SC = O(m*n)
from copy import deepcopy

class Solution:
    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        minutes = 0

        while True:

            changed = False

            temp = deepcopy(grid)

            for r in range(rows):
                for c in range(cols):

                    if grid[r][c] == 2:

                        directions = [(1,0),(-1,0),(0,1),(0,-1)]

                        for dr, dc in directions:

                            nr = r + dr
                            nc = c + dc

                            if 0 <= nr < rows and 0 <= nc < cols:

                                if grid[nr][nc] == 1:

                                    temp[nr][nc] = 2
                                    changed = True

            grid = temp

            if not changed:
                break

            minutes += 1

        for row in grid:
            if 1 in row:
                return -1

        return minutes


    

"""
Now something clicks.

I need a data structure that processes things level by level.

That immediately reminds me of Breadth-First Search (BFS).

Even better, since there are multiple starting rotten oranges, I should start BFS from 
all of them at once.

That's how I naturally arrive at the Multi-Source BFS solution—not by memorizing 
the pattern, but by identifying the inefficiency in the brute-force simulation 
and asking how to avoid repeatedly scanning the whole grid.
"""




# TC = O(R * C) where R is rows and c is columns and SC = O(R * C)
from collections import deque

def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    fresh_count = 0
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh_count += 1
    minutes_passed = 0
    while len(queue) != 0 and fresh_count > 0:
        minutes_passed += 1
        total_rotten = len(queue)
        for _ in range(total_rotten):
            i , j  = queue.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i = i + dx
                new_j = j + dy
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                    continue
                if grid[new_i][new_j] == 0 or grid[new_i][new_j] == 2:
                    continue
                fresh_count -= 1
                grid[new_i][new_j] = 2
                queue.append((new_i,new_j))
    if fresh_count > 0:
        return - 1
    return minutes_passed
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))