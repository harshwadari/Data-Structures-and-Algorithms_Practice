# Closest Binary Tree Value 
"""
Given root of a Binary Search Tree (BST) and an integer k, find the minimum absolute difference between k and the value of any node in the BST.

Examples:

Input: root = [10, 2, 11, 1, 5, N, N, N, N, 3, 6, N, 4], k = 13

Output: 2
Explanation: The node with value 11 is closest to k = 13. So, the minimum absolute difference is |11 - 13| = 2.
Input: root = [8, 1, 9, N, 4, N, 10, 3], k = 9

Output: 0
Explanation: The node with value 9 is closest to k = 9. So, the minimum absolute difference is |9 - 9| = 0.
Constraints:

1 ≤ size of binary tree, k ≤ 105
0 ≤ Node.data ≤ 105
"""

# Optimal Approach using InOrder Traversal 
# TC = O(N) and SC = O(H) where  h is height of tree
'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root, k: int) -> int:
        # code here
        minvalue = float('inf')
        def dfs(node):
            nonlocal minvalue
            if node is None:
                return None
            dfs(node.left)
            minvalue = min(minvalue,abs(k-node.data))
            dfs(node.right)
            return minvalue
        return dfs(root)



# Another approach using BFS
'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''
from queue import deque
class Solution:
    def minDiff(self, root,k) -> int:
        # code here
        if root is None:
            return -1
        queue = deque()
        queue.append(root)
        minvalue = float('inf')
        while len(queue) != 0:
            node = queue.popleft()
            minvalue = min(minvalue,abs(k - node.data))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return minvalue