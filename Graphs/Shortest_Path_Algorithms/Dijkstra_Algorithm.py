# Dijkstra Algorithm
"""
Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, 
represented by 2d array edges[][], where edges[i]=[u, v, w] represents the edge between the 
nodes u and v having w edge weight.
You have to find the shortest distance of all the vertices from the source vertex src, 
and return an array of integers where the ith element denotes the shortest distance 
between ith node and source vertex src.

Note: The Graph is connected and doesn't contain any negative weight edge.
It is guaranteed that all the shortest distance will fit in a 32-bit integer.
"""

import heapq

class Solution:
    def dijkstra(self, V, edges, src):

        adjlist = [[] for _ in range(V)]

        for u, v, d in edges:
            adjlist[u].append((v, d))
            adjlist[v].append((u, d))

        distance = [float('inf')] * V
        distance[src] = 0

        queue = [(0, src)]

        while queue:

            current_distance, node = heapq.heappop(queue)

            if current_distance > distance[node]:
                continue

            for adjnode, weight in adjlist[node]:

                new_distance = current_distance + weight

                if new_distance < distance[adjnode]:
                    distance[adjnode] = new_distance
                    heapq.heappush(queue, (new_distance, adjnode))

        return distance


# Dijkstras Algorithm  using set appraoch 
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adjlist = [[] for _ in range(V)]
        for u , v , d in edges:
            adjlist[u].append((v,d))
            adjlist[v].append((u,d))
        distance = [float('inf')] * V
        distance[src] = 0
        myset = set()
        myset.add((0,src))
        while len(myset) != 0:
            dist,node = min(myset)
            myset.discard((dist,node))
            for adjnode,weight in adjlist[node]:
                travel = dist + weight
                if travel < distance[adjnode]:
                    if distance[adjnode] != float('inf'):
                        myset.discard((distance[adjnode],adjnode))
                    distance[adjnode] = travel
                    myset.add((travel,adjnode))
        return distance