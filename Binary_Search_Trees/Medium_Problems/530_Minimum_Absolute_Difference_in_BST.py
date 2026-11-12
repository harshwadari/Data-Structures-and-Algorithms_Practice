# 530. Minimum Absolute Difference in BST
"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""

# TC = O(2N) and SC = O(N)

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = []
        def helper(root):
            if root is None:
                return None
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        helper(root)
        ans = float('inf')
        for  i in range(1,len(result)):
            ans = min(ans,abs(result[i] - result[i-1]))
        return ans


# Optimal Approach without extra space
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        prev = None
        ans = float('inf')
        def helper(node):
            nonlocal prev,ans
            if node is None:
                return 
            helper(node.left)
            if prev is not None:
                ans = min(ans,node.val - prev)
            prev = node.val
            helper(node.right)
        helper(root)
        return ans

# Another Approach using BFS Algorithm 

from collections import deque

class Solution(object):
    def minDiffInBST(self, root):
        q = deque()
        q.append(root)

        values = []

        while len(q) > 0:
            node = q.popleft()

            values.append(node.val)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

        values.sort()

        ans = float('inf')

        for i in range(1, len(values)):
            diff = values[i] - values[i - 1]

            if diff < ans:
                ans = diff

        return ans