"""
first we will learn how to store a graph in memory.
we will learn about two common ways to represent a graph in memory: adjacency list and adjacency matrix.
"""

# adjacency matrix 

n = 5 # number of vertices
m = 6 # number or edges

edges = [[1,2],[1,3],[2,3],[2,4],[3,4],[4,5]]

# 1 based indexing graph
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for u , v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1
print(matrix)


# adjacency list
n = 5
m = 6
edges = [[1,2],[1,3],[2,3],[2,4],[3,4],[4,5]]

#list 
adj_list = [[]for _ in range(n+1)] 

for u , v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
print(adj_list)