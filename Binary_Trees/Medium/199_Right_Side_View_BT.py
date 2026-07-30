# 199. Binary Tree Right Side View
"""
Given the root of a binary tree, imagine yourself standing on the right side of 
it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Level Order BFS Approach 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC = O(N) and SC = O(N) + O(N) result and queue space 
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if i == level - 1:
                    result.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return result


# DFS Approach 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TC = O(N) and SC = O(H) stack space 
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def reverse(node,level,ans):
            if node is None:
                return 
            if len(ans) == level:
                ans.append(node.val)
            if node.right != None:
                reverse(node.right,level + 1,ans)
            if node.left != None:
                reverse(node.left,level + 1,ans)
        reverse(root,0,ans)
        return ans