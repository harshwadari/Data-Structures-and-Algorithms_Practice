# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance


"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [
fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and 
toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and 
whose distance is at most distanceThreshold, If there are multiple such cities, return the city 
with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' 
weights along that path.

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return 
city 3 since it has the greatest number.

Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""





class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adjmat = [[float('inf') for _ in range(n)]for _ in range(n)]
        for u,v,w in edges:
            adjmat[u][v] = w
            adjmat[v][u] = w
        for i in range(n):
            adjmat[i][i] = 0
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adjmat[i][via] != float('inf') and adjmat[via][j] != float('inf'):
                        adjmat[i][j] = min(adjmat[i][j] , adjmat[i][via] + adjmat[via][j])
        min_neigh = n
        city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if adjmat[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_neigh:
                min_neigh = count
                city = i
        return city