# 210. Course Schedule II
"""
There are a total of numCourses courses you have to take, labeled 
from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first 
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have 
to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is impossible 
to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 
you should have finished course 0. So the correct course order is [0,1].

"""

# BFS approach khans algorithm
"""

------------------------------------------------------------
Time Complexity
------------------------------------------------------------

| Operation                                    | Complexity |
|----------------------------------------------|------------|
| Create adjacency list                        | O(V)       |
| Initialize indegree array                    | O(V)       |
| Insert all edges into adjacency list         | O(E)       |
| Compute indegree of each vertex              | O(E)       |
| Push all 0-indegree vertices into queue      | O(V)       |
| Kahn's BFS (visit every vertex once)         | O(V)       |
| Traverse all adjacency lists (all edges)     | O(E)       |
| Overall Time Complexity                      | O(V + E)   |


------------------------------------------------------------
Space Complexity
------------------------------------------------------------

| Data Structure            | Complexity |
|---------------------------|------------|
| Adjacency List            | O(V + E)   |
| Indegree Array            | O(V)       |
| Queue                     | O(V)       |
| Result Array              | O(V)       |
| Overall Space Complexity  | O(V + E)   |

"""
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u,v in prerequisites:
            adjlist[v].append(u)
            indegree[u] += 1
        queue = deque()
        result = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node)
            for adjnode in adjlist[node]:
                indegree[adjnode] -= 1
                if indegree[adjnode] == 0:
                    queue.append(adjnode)
        if len(result) == numCourses:
            return result
        return []   