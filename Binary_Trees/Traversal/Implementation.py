# Implementation of tree 

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
cola = Node("cola")
fanta = Node("fanta")
tea = Node("tea")
coffee = Node("coffee")

drinks.left = hot
drinks.right = cold
hot.left = tea
hot.right = coffee
cold.left = cola
cold.right = fanta

print(drinks.right.left.val)
print(hot.right.val)




"""
Tree Traversal
1. Depth  First Search :
   Inorder   
   Preorder 
   Postorder 

2. Breadth First Search:
    Levelorder 

"""