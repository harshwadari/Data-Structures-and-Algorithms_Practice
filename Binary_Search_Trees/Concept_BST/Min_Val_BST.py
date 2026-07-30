# Minimum in BST
"""
Given the root of a Binary Search Tree, find the minimum element in this given BST.
"""

# Optimal Appraoch using BST
# TC = O(LogN) and SC = O(1)
def MINBST(root):
    while root and root.left:
        root = root.left
    return root.data