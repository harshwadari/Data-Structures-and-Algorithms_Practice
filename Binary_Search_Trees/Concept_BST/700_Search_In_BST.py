# 700. Search in a Binary Search Tree


# BST Formula = Left < Root < Right


"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree 
rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""
from collections import deque
# TC = O(N) and SC = O(N) where n is height of tree
# BFS Appraoch without using Binary Search
def BST(root,val):
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        node = queue.popleft()
        if node.val == val:
            return node
        else:
            if node.left is not  None:
                queue.append(node.left)
            if node.right is not  None:
                queue.append(node.right)
    return None


# Opitmal Approach using BST
# TC = O(logN) and SC = O(1)
def SearchBST(root,val):
    while root is not None:
        if root.val == val:
            return root
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    return None