# Floyd Warshall Algorithm


"""
You are given a weighted directed graph, represented by an adjacency matrix, dist[][] of size n x n, 
where dist[i][j] represents the weight of the edge from node i to node j. If there is no direct edge,
dist[i][j] is set to a large value (i.e., 108) to represent infinity.
The graph may contain negative edge weights, but it does not contain any negative weight cycles.

Your task is to find the shortest distance between every pair of nodes i and j in the graph.

Note: Modify the distances for every pair in place.

Examples :

Input: dist[][] = [[0, 4, 108, 5, 108], [108, 0, 1, 108, 6], [2, 108, 0, 3, 108], 
[108, 108, 1, 0, 2], [1, 108, 108, 4, 0]]

Output: [[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]

Constraints:
1 ≤ dist.size() ≤ 100
-1000 ≤ dist[i][j] ≤ 1000
dist[i][j] can be 108 to represent infinity.


"""
# TC = O(N^3) and SC = O(N^2)
def floydwarshall(dist):
    n = len(dist)
    for via in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][via] != 10 ** 8 and dist[via][j] != via:
                    dist[i][j] = min(dist[i][j] ,dist[i][via]+dist[via][j])
    return dist