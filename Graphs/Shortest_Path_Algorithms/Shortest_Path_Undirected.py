# Shortest Path in Unweighted Graph
"""
Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, 
where edges[i] = [u, v] denotes an undirected edge between vertex 
u and vertex v, given two vertices src and dest, find the length of 
the shortest path from src to dest. If there is no path between src and dest, return -1.

Note: All edges have a unit weight of 1.

Examples :

Input: V = 9, edges[][] = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], 
[2, 6], [5, 6], [6, 7], [6, 8], [7, 8]], src = 0, dest = 8
Output: 4
Explanation: One of the shortest paths from vertex 0 to vertex 8 
is 0 -> 1 -> 2 -> 6 -> 8, which contains 4 edges.
"""
# Single Source Shortest Path
# BFS Appraoch 

from collections import deque
class Solution:
    def shortestPath(self, V, edges, src, dest):
        # code here
        adjlist = [[] for _ in range(V)]
        distance = [-1] * V
        for u , v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        queue = deque()
        queue.append([src,0])
        distance[src] = 0
        while len(queue)!= 0:
            node,travel = queue.popleft()
            for adjnode in adjlist[node]:
                if distance[adjnode] == -1:
                    distance[adjnode] = travel + 1
                    queue.append([adjnode,travel + 1])
        return distance[dest]