# pre order travesal of binary tree  [Root - Left - Right]

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
eight = Node(8)
nine = Node(9)
ten = Node(10)

five.left = three
five.right = four
three.left = two
three.right = nine
four.left = eight
four.right = ten
eight.left = one
eight.right = six

# print(five.right.right.val)
# print(five.left.right.val)


# preorder travesal 
# Preorder Means root comes first and left and right 
def preOrder_traversal(node):
    if node == None:
        return 
    print(node.val,end="-")
    preOrder_traversal(node.left)
    preOrder_traversal(node.right)

preOrder_traversal(five)



# leetcode pre order traversal


# TC = O(N) and SC O(H) where h is height of tree
def preorder_traversal(self,root):
    if root == None:
        return []
    result = []
    result.append(root.val)
    result += self.preorder_traversal(root.left)
    result += self.preorder_traversal(root.right)
    return result


# Iterative approach 

def preorderTraversal(self, root):
    if root == None:
        return []
    result = []
    stack = [root]
    while stack :
        node = stack.pop()
        result.append(node.val)
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
    return result