# Linked List Insert at Head - Easy OA Style

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_at_head(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node


# -------- DRIVER CODE --------
n = int(input())                 # number of nodes

values = list(map(int, input().split()))

x = int(input())                 # value to insert at head

# build linked list
head = None
tail = None

for v in values:
    node = Node(v)
    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node

# insert at head
head = insert_at_head(head, x)

# print linked list
temp = head
while temp:
    print(temp.val, end=" ")
    temp = temp.next




# inset at end


def insert_at_end(head, val):
    new_node = Node(val)

    if head is None:
        return new_node

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    return head
