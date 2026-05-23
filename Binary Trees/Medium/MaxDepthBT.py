# max depth of binary tree


# TC = O(N) and SC = O(1)
def maxDepth(self,root):
    if root == None:
        return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return 1 + max(left,right)
