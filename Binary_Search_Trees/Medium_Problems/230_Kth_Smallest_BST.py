# 230. Kth Smallest Element in a BST
"""
Given the root of a binary search tree, and an integer k, return the kth smallest value 
(1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) 
and you need to find the kth smallest frequently, how would you optimize?
"""

# Brute Approach using level order traversal and sorting of result array
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC = O(NlogN) and SC = O(N)
from collections import deque
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        result = []
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        result.sort()
        return result[k - 1]


# Better Appraoch using In-Order Traversal which requires no sorting 
# TC = O(N) and SC =  O(N)
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        result = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result[k - 1]


# More better approach is to not use result use count and return node when count equals k
# TC = O(N) and SC = O(N)
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = 0
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k: # for kth largest if count == k : return N - k
                return curr.val
            curr = curr.right # For kth largest just return len(result) - k



# Optimal Approach using Morris In-Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        count = 0
        curr = root

        # TC: O(n)
        # SC: O(1)
        while curr is not None:

            # No left subtree
            if curr.left is None:
                count += 1

                if count == k:
                    return curr.val

                curr = curr.right

            else:
                # Find inorder predecessor
                predecessor = curr.left

                # TC of all predecessor traversals together = O(n)
                while predecessor.right is not None and predecessor.right != curr:
                    predecessor = predecessor.right

                # Create thread
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left

                # Thread already exists
                else:
                    predecessor.right = None

                    count += 1

                    if count == k:
                        return curr.val

                    curr = curr.right
