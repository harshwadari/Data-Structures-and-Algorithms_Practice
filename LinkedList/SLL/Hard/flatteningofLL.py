# Flattening of a Linked List

# brute force approach using array 
#Tc = O(NlogN) and SC = O(N) where N is total number of nodes in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None
def flatterll(root):
    if not root:
        return root
    arr = []
    temp = root
    while temp is not None:
        curr = temp
        while curr is not None:
            arr.append(curr.data)
            curr = curr.bottom
        temp = temp.next
    arr.sort(0)
    dummyNode = Node(0)
    temp = dummyNode
    for val in arr:
        temp.bottom = Node(val)
        temp = temp.bottom
    return dummyNode.bottom