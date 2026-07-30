# Bottom View of Binary Tree

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return None
        result = {}
        ans = []
        queue = deque()
        queue.append([root,0])
        while len(queue) != 0:
            node,line = queue.popleft()
            result[line] = node.data
            if node.left is not None:
                queue.append([node.left,line - 1])
            if node.right is not None:
                queue.append([node.right,line + 1])
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans
            
    
            
            
            
            
