# 787. Cheapest Flights Within K Stops
"""
There are n cities connected by some number of flights. You are given an array 
flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight 
from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from 
src to dst with at most k stops. If there is no such route, return -1.

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, 
dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 
600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""

# Optimal approach using dijkstra algorithm 
from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adjlist = [[] for _ in range(n)]
        distance = [float('inf')] * n
        for u, v , cost in flights:
            adjlist[u].append([v,cost])
        distance[src] = 0
        queue = deque()
        queue.append([0,src,0])
        while len(queue) != 0:
            step,node,cost = queue.popleft()
            for adjnode , price in adjlist[node]:
                newcost = cost + price
                if newcost < distance[adjnode]:
                    newstep = step + 1
                    if newstep == k + 1:
                        if adjnode != dst:
                            continue
                    distance[adjnode] = newcost
                    queue.append([newstep,adjnode,newcost])
        if distance[dst] == float('inf'):
            return - 1
        return distance[dst]