"""
first we will learn how to store a graph in memory.
we will learn about two common ways to represent a graph in memory: adjacency list and adjacency matrix.
"""

# adjacency matrix 
"""
Time Complexity

Create matrix:

O(V²)

Insert edges:

O(E)

Total:

O(V² + E)

Since

E ≤ V²

we usually write

O(V²)
Space Complexity

Matrix size:

V × V

Therefore

O(V²)
"""
n = 5 # number of vertices
m = 6 # number or edges

edges = [[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# 1 based indexing graph
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for u , v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1
print(matrix)


# adjacency list
"""
Time Complexity

Creating empty list:

O(V)

Traversing all edges:

O(E)

Total:

O(V + E)
Space Complexity

Adjacency list itself:

O(V + E)

Reason:

V empty lists.
Total stored neighbors:
Directed → E
Undirected → 2E

Overall:

O(V + E)
"""
n = 5
m = 6
edges = [[1,2],[1,3],[2,3],[2,4],[3,4],[4,5]]

#list 
adj_list = [[]for _ in range(n+1)] 

for u , v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
print(adj_list)