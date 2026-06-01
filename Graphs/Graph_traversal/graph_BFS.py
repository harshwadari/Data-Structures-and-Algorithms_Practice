# BFS Traversal of a graph

# TC = O(N) + O(E where E is no. of edges and SC = O(3N)
from collections import deque
class Solution:
    def bfs(self, adj):
        # code here
        n = len(adj)
        start_node = 0
        result = []
        queue = deque()
        visited = [0] * (n + 1)
        queue.append(start_node)
        visited[start_node] = 1
        while len(queue) != 0:
            e = queue.popleft()
            result.append(e)
            for node in adj[e]:
                if visited[node] == 0:
                    queue.append(node)
                    visited[node] = 1
        return result
        