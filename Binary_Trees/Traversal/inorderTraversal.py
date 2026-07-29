# Inorder Traversal of Tree
# Inorder works by Left - Root - Right 
# TC = O(N) and SC = O(H) where h is height of tree

# Inorder means root is in (in) position 
# Recursive Solution 
def inorder(self,root):
    if root == None:
        return []
    result = []
    result += self.inorder(root.left)
    result.append(root.val)
    result += self.inorder(root.right)
    return result


# Iterative Solution 
def Inorder(root):
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
    return result 

