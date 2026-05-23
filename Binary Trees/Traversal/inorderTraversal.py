# Inorder Traversal of Tree
# Inorder works by Left - Root - Right 
# TC = O(N) and SC = O(H) where h is height of tree

def inorder(self,root):
    if root == None:
        return []
    result = []
    result += self.inorder(root.left)
    result.append(root.val)
    result += self.inorder(root.right)
    return result