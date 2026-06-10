# To find max diamter of binary tree LC 543

# naive approach is to find height of left and right subtree for each node and update diameter but it will take O(N^2) time
# TC = O(N) and SC = O(H) where h is height of tree
def diameterOfBinaryTree(self,root):
    diameter = 0
    def height(node):
        nonlocal diameter
        if node == None:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter,left + right)
        return 1 + max(left,right)
    height(root)
    return diameter