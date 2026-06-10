# check for balanced binary tree LC 110
# TC = O(N) and SC = O(H) where h is height of tree
def isBalanced(self,root):
    def height(node):
        if node == None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left,right)
    if height(root) == -1:
        return False
    return True
# changes made