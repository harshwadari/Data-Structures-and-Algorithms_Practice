# 450. Delete Node in a BST
"""
Given a root node reference of a BST and a key, delete the node with the given key in 
the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
"""


"""
Overall TC = O(h)
Balanced BST: O(log n)
Skewed BST: O(n)
Overall Space Complexity

This solution is iterative.

No recursion
No stack
No extra data structures
Overall SC = O(1)
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        # TC: O(1)
        # SC: O(1)
        self.val = val
        self.left = left
        self.right = right

    def findRight(self, node):
        # Finds the rightmost node in a subtree.
        # TC: O(h)
        # SC: O(1)
        while node.right is not None:
            node = node.right
        return node

    def deletion(self, node):
        # Deletes the given node and reconnects the BST.
        # TC: O(h) (because findRight() may traverse the subtree)
        # SC: O(1)

        if node.left is None:
            return node.right

        elif node.right is None:
            return node.left

        else:
            right_child = node.right

            # O(h)
            last_right = self.findRight(node.left)

            # O(1)
            last_right.right = right_child

            return node.left

    def deleteNode(self, root, key):
        # Search for the node iteratively.
        # TC: O(h)
        # SC: O(1)

        if root is None:
            return None

        if root.val == key:
            # deletion() = O(h)
            return self.deletion(root)

        temp = root

        while temp is not None:

            if temp.val > key:

                if temp.left is not None and temp.left.val == key:
                    # O(h)
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    # O(1)
                    temp = temp.left

            else:

                if temp.right is not None and temp.right.val == key:
                    # O(h)
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    # O(1)
                    temp = temp.right

        return root