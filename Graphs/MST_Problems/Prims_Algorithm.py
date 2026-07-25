# Minimum Spanning Tree / Prims Algorithm
# Prim’s Algorithm builds the MST by greedily picking the smallest edge that connects 
# a new node to the tree, ensuring no cycles are formed.

"""
Given a weighted, undirected, and connected graph with V vertices and E edges, your 
task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) 
of the graph. The graph is provided as a list of edges, where each edge is represented as 
[u, v, w], indicating an edge between vertex u and vertex v with edge weight w.

Input: V = 3, E = 3, Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
 
Output: 4
Explanation:
The Spanning Tree resulting in a weight
of 4 is shown above


Constraints:
2 ≤ V ≤ 1000
V-1 ≤ E ≤ (V*(V-1))/2
1 ≤ w ≤ 1000
The graph is connected and doesn't contain self-loops & multiple edges.


"""
"""
Overall TC = O(V + E) + O(E log E)
           = O(E log E)

SC = O(V + E)
     O(V) -> visited
     O(V) -> priority queue (can grow up to O(E) in worst case)
     O(E) -> adjacency list
"""

import heapq

class Solution:
    def spanningTree(self, V, edges):
        # code here
        adjlist = [[] for _ in range(V)]   # O(V)

        for u, v, w in edges:              # O(E)
            adjlist[u].append([v, w])
            adjlist[v].append([u, w])

        visited = [0] * V                  # O(V)

        mst = []
        total = 0

        queue = []
        queue.append([0, 0, -1])           # O(1)

        while len(queue) != 0:             # Heap operations happen O(E) times
            wt, node, parent = heapq.heappop(queue)   # O(log E)

            if visited[node] == 0:
                visited[node] = 1

                if parent != -1:
                    total += wt
                    mst.append([parent, node])

                for adjnode, wt in adjlist[node]:     # Total across all nodes = O(E)
                    if visited[adjnode] == 0:
                        heapq.heappush(queue, [wt, adjnode, node])  # O(log E)

        return total