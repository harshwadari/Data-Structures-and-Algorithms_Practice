# 797. All Paths From Source to Target
"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all 
possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from 
node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""

# Optimal Appraoch using dfs and backtracking
"""

------------------------------------------------------------
Time Complexity
------------------------------------------------------------

| Operation                                    | Complexity |
|----------------------------------------------|------------|
| DFS traversal of all possible paths          | O(P × V)   |
| Copy path using temp[:]                      | O(V)       |
| Enumerate all P valid paths                  | O(P × V)   |
| Overall Time Complexity                      | O(P × V)   |
| Worst-case Time Complexity                   | O(V × 2^V) |


------------------------------------------------------------
Space Complexity
------------------------------------------------------------

| Data Structure            | Complexity |
|---------------------------|------------|
| Current path (temp)       | O(V)       |
| Recursion stack           | O(V)       |
| Result (all paths)        | O(P × V)   |
| Overall Space Complexity  | O(P × V)   |
| Worst-case Space          | O(V × 2^V) |

where:
P = number of valid paths from source to target
V = maximum number of vertices in a path

"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        result = []
        def dfs(source,target,temp):
            temp.append(source)
            if source == target:
                result.append(temp[:])
                temp.pop()
                return
            for neighbour in graph[source]:
                dfs(neighbour,target,temp)
            temp.pop()
        dfs(0,len(graph)-1,[])
        return result

    






# same problem but instead of result arr return count of all possible paths but in bigger constraints
# constrainst are nodes = 10 ^ 5
# recusion dfs backtracking approach 
def countPaths(V, edges, src, dest):
    adjlist = [[] for _ in range(V)]
    for u , v in edges:
        adjlist[u].apend(v)
    result = []
    def dfs(src,dest,temp):
        temp.append(src)
        if src == dest:
            result.append(temp[:])
            temp.pop()
            return
        for node in adjlist[src]:
            dfs(node,dest,temp)
        temp.pop()
    dfs(src,dest,[])
    return len(result)



# the above backtracking appraoch will give tle so we can memoize that and be optimal for larger constraints
def countpathsmemo(V,edges,src,dest):
    adjlist = [[] for _ in range(V)]
    for u , v in edges:
        adjlist[u].append(v)
    dp = [-1] * V
    def dfs(node):
        if src == dest:
            return 1
        if dp[node] != -1:
            return dp[node]
        count = 0
        for neigh in adjlist[node]:
            count += dfs(neigh)
        dp[node] = count
        return count
    return dfs(src)