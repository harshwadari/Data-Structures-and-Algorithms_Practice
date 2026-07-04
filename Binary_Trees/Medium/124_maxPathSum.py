class Solution:
    maxi = float('-inf')
    def maxsum(self,root):
        if root == None:
            return 0
        leftsum = self.maxsum(root.left)
        if leftsum < 0:
            leftsum = 0
        rightsum = self.maxsum(root.right)
        if rightsum < 0:
            rightsum = 0
        self.maxi = max(self.maxi,leftsum + rightsum + root.data)
        return max(leftsum,rightsum) + root.data
    def findMaxSum(self, root): 
        # code here
        self.maxsum(root)
        return self.maxi
    

# TC = O(N) and SC = O(H)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi = [float('-inf')]
        def maxsum(root):
            if root == None:
                return 0
            leftsum = maxsum(root.left)
            if leftsum < 0:
                leftsum = 0
            rightsum = maxsum(root.right)
            if rightsum < 0:
                rightsum = 0
            maxi[0] = max(maxi[0],leftsum + rightsum + root.val)
            return root.val + max(leftsum, rightsum)
        maxsum(root)
        return maxi[0]