# 3310. Remove Methods From Project
"""
You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations,
where invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, 
either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any 
methods within it.

Return an array containing all the remaining methods after removing all the suspicious 
methods. You may return the answer in any order. If it is not possible to remove all the 
suspicious methods, none should be removed.

 

Example 1:

Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

Output: [0,1,2,3]

Explanation:



Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, 
which are not suspicious. We return all elements without removing anything.

Example 2:

Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

Output: [3,4]

Explanation:



Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. 
We can remove them.

Example 3:

Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

Output: []

Explanation:



All methods are suspicious. We can remove them.

 

Constraints:

1 <= n <= 105
0 <= k <= n - 1
0 <= invocations.length <= 2 * 105
invocations[i] == [ai, bi]
0 <= ai, bi <= n - 1
ai != bi
invocations[i] != invocations[j]
"""


# Optimal Approach  Using DFS
def remainingMethodDFS(n:int,k:int,invocations:list[list[int]]) -> list[int] :
    adjlist = [[] for _ in range(n)]
    for u,v in invocations:
        adjlist[u].append(v)
    visited  = [0] * n
    result = []
    def dfs(node):
        visited[node] = 1
        for adjnode in adjlist[node]:
            if visited[adjnode]  == 0:
                visited[adjnode] = 1
                dfs(adjnode)
    dfs(k)
    for u,v in invocations:
        if visited[u] == 0 and visited[v] == 1:
            return list(range(n))
    for i in range(n):
        if visited[i] == 0:
            result.append(i)
    return result 




# Optimal Approach using BFS
from collections import deque

# Overall Time Complexity:
# Without constants: O(V + E)
# With constants: O(2V + 2E) ≈ O(V + E)

# Overall Space Complexity:
# Without constants: O(V + E)
# With constants: O(3V + E)
# (Adjacency List = V + E, Visited = V, Queue = V, Result = V in worst case)

def removingMethodsBFS(n: int, k: int, invocations: list[list[int]]) -> list[int]:
    result = []                          # TC = O(1)              SC = O(V) worst case
    adjlist = [[] for _ in range(n)]     # TC = O(V)              SC = O(V)

    for u, v in invocations:             # TC = O(E)
        adjlist[u].append(v)             # TC = O(1)

    visited = [0] * n                    # TC = O(V)              SC = O(V)

    queue = deque()                      # TC = O(1)              SC = O(V) worst case
    queue.append(k)                      # TC = O(1)
    visited[k] = 1                       # TC = O(1)

    while len(queue) != 0:               # TC = O(V + E)
        node = queue.popleft()           # TC = O(1)

        for adjnode in adjlist[node]:    # Overall TC = O(E)
            if visited[adjnode] == 0:    # TC = O(1)
                visited[adjnode] = 1     # TC = O(1)
                queue.append(adjnode)    # TC = O(1)

    for u, v in invocations:             # TC = O(E)
        if visited[u] == 0 and visited[v] == 1:
            return list(range(n))        # TC = O(V)  SC = O(V)

    for i in range(n):                   # TC = O(V)
        if visited[i] == 0:
            result.append(i)             # TC = O(1)

    return result                        # TC = O(1)