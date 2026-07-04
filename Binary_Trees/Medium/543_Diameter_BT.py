# 543. Diameter of Binary Tree
"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Optimal approach using recursion 
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
# TC = O(N) and SC = O(N)
class Solution:
    def diameter(self, root):
        # code here
        diameter = [0]
        def height(root):
            if root == None:
                return 0
            left = height(root.left)
            right = height(root.right)
            diameter[0] = max(diameter[0] , left + right)
            return 1 + max(left,right)
        height(root)
        return diameter[0]