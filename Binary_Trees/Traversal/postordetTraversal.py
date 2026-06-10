# Postorder Traversal of Tree
# TC = O(N) and SC = O(H) where h is height of tree

def postorder(self,root):
    if root == None:
        return []
    result = []
    result += self.inorder(root.left)
    result += self.inorder(root.right)
    result.append(root.val)
    return result