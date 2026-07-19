# 1976. Number of Ways to Arrive at Destination
"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with 
bi-directional roads between some intersections. The inputs are generated such that
 you can reach any intersection from any other intersection and that there is at most 
 one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] 
means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of 
time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:


Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],
[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 
6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it
 takes 10 minutes.
 

Constraints:

1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
There is at most one road connecting any two intersections.
You can reach any intersection from any other intersection.
"""

# Optimal Appraoch using dijkstra Algorithm
"""
+--------------------------------------------------+----------------------------+
|                    Operation                     |        Complexity          |
+--------------------------------------------------+----------------------------+
| Build Adjacency List                             | O(m)                       |
| Initialize Distance & Ways Arrays                | O(n)                       |
| Initialize Min Heap                              | O(1)                       |
| Push Source Node                                 | O(log n)                   |
| Pop from Min Heap (per operation)                | O(log n)                   |
| Relax an Edge                                    | O(log n)                   |
| Process All Edges using Dijkstra                 | O((n + m) log n)           |
| Count Number of Shortest Paths                   | O(1) per relaxation        |
+--------------------------------------------------+----------------------------+
| Overall Time Complexity                          | O((n + m) log n)           |
+--------------------------------------------------+----------------------------+


+--------------------------------------------------+----------------------------+
|                 Space Usage                      |        Complexity          |
+--------------------------------------------------+----------------------------+
| Adjacency List                                  | O(n + m)                   |
| Distance Array                                  | O(n)                       |
| Ways Array                                      | O(n)                       |
| Priority Queue (Worst Case)                     | O(m)                       |
+--------------------------------------------------+----------------------------+
| Overall Space Complexity                        | O(n + m)                   |
+--------------------------------------------------+----------------------------+


Explanation:
------------
n = Number of cities (vertices)
m = Number of roads (edges)

• The adjacency list stores every road twice because the graph is
  undirected, requiring O(n + m) space.

• Dijkstra's algorithm processes every edge while maintaining a
  min-heap. Every push/pop operation costs O(log n), resulting in
  O((n + m) log n) time.

• The 'ways' array is updated during edge relaxation itself, so
  counting shortest paths does not require an additional traversal.

• Therefore,

        Time Complexity  : O((n + m) log n)
        Space Complexity : O(n + m)
"""
import heapq
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        adjlist = [[] for _ in range(n)]
        for u,v,d in roads:
            adjlist[u].append([v,d])
            adjlist[v].append([u,d])
        distance = [float('inf')] * n
        ways = [0] * n
        distance[0] = 0
        ways[0] = 1
        queue = [[0,0]] # distance,node
        while len(queue) != 0:
            dist,node = heapq.heappop(queue)
            for adjnode ,weight in adjlist[node]:
                new_dist = dist + weight
                if new_dist < distance[adjnode]:
                    distance[adjnode] = new_dist
                    heapq.heappush(queue,[new_dist,adjnode])
                    ways[adjnode] = ways[node]
                elif new_dist == distance[adjnode]:
                    ways[adjnode] = (ways[adjnode]+ways[node]) * MOD
        return ways[n - 1] % MOD



