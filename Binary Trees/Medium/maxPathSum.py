class Solution:
    maxi = float("-inf")

    def findMaxPathSum(self, root):
        if not root:
            return 0

        # Recursively get max path sums from left and right children
        leftPathSum = self.findMaxPathSum(root.left)
        rightPathSum = self.findMaxPathSum(root.right)

        # If a path contributes negatively, ignore it
        if leftPathSum < 0:
            leftPathSum = 0
        if rightPathSum < 0:
            rightPathSum = 0

        # Update global maximum: best path that passes through this node
        self.maxi = max(self.maxi, leftPathSum + root.val + rightPathSum)

        # Return best single-branch path sum to parent
        return max(leftPathSum, rightPathSum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxPathSum(root)
        return self.maxi