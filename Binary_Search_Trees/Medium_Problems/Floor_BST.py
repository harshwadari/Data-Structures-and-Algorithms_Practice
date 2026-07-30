# Find the floor value in a Binary Search Tree
# TC = O(logN) where n  is height of tree and SC = O(1)
def FloorBST(root,x):
    floor = -1
    while root is not None:
        if root.val <= x:
            floor = root.val
            root = root.right
        else:
            root = root.right
    return floor 