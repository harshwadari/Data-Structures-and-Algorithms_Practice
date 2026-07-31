# Morris Traversal 
"""
Morris Algorithm for tree traversal, a space-optimized technique that performs both 
Inorder and Preorder traversals without using recursion or stack. This algorithm achieves 
O(1) space complexity by temporarily threading the binary tree, making it perfect for 
memory-constrained environments.
Morris Traversal is based on the concept of Threaded Binary Trees and works by creating 
temporary links to inorder predecessors, allowing us to navigate back to parent nodes 
without additional data structures.
"""
# Morris traversal of inorder Left -> Root -> Right
# TC = O(N) and SC = O(1)
class Solution:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right 
    def MorrisIN(self,root):
        if root is None:
            return None
        result = []
        current = root
        while current is not None:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)    # this line changed for pre order traversal            
                    current = current.right
        return result 


# Pre Order Traversal Using Morris  Root -> Left -> Right 


class Solution:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right 
    def MorrisPre(self,root):
        if root is None:
            return None
        result = []
        current = root
        while current is not None:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    result.append(current.val)
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None              
                    current = current.right
        return result 