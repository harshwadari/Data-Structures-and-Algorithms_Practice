# 994. Rotting Oranges


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