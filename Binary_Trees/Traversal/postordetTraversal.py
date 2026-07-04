# Postorder Traversal of Tree [ Left - Right - Root]
# TC = O(N) and SC = O(H) where h is height of tree
# post means root is in last part before left and right 
def postorder(self,root):
    if root == None:
        return []
    result = []
    result += self.inorder(root.left)
    result += self.inorder(root.right)
    result.append(root.val)
    return result

# Iterative approach 
class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        result = []
        lastVisited = None

        while root or stack:

            while root:
                stack.append(root)
                root = root.left

            node = stack[-1]

            if node.right and lastVisited != node.right:
                root = node.right
            else:
                result.append(node.val)
                lastVisited = stack.pop()

        return result