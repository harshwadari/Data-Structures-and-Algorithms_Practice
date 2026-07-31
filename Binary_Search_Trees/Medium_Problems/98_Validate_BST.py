# 98. Validate Binary Search Tree
"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

"""

# TC = O(N) and SC = O(N) stack space 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,node,range):
        if node is None:
            return True
        if not range[0] < node.val < range[1]:
            return False
        left = self.dfs(node.left,[range[0],node.val])
        if left == False:
            return False
        right = self.dfs(node.right,[node.val,range[1]])
        if left == True and right == True:
            return True
        return False
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.dfs(root,[float('-inf'),float('inf')])