# A binary tree Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# TC = O(N) where N is  number of nodes and SC = O(N) result space 
from queue import deque
class Solution:
    def levelOrder(self, root):
        # code here
        result = []
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            e = queue.popleft()
            result.append(e.data)
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
        return result