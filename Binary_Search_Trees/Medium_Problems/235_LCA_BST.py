# 235. Lowest Common Ancestor of a Binary Search Tree
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of 
two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is 
defined between two nodes p and q as the lowest node in T that has both p and q as 
descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant 
of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""



# LCA in BT
# TC = O(N) and SC = O(N) stack space
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node,p,q):
            if node is None:
                return None
            if node == p or node == q:
                return node
            left = dfs(node.left,p,q)
            right = dfs(node.right,p,q)
            if left is None and right is None:
                return None
            elif left is None:
                return right
            elif right is None:
                return left
            return node
        return dfs(root,p,q)





# LCA in BST
# TC = O(N) and SC = O(1) n is heigh of tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root
        while True:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p == curr.val:
                return p
            elif q == curr.val:
                return q
            else:
                return curr