class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None
class myStack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return -1

        popped = self.top.data
        self.top = self.top.next

        return popped

    def peek(self):
        if self.top is None:
            return -1

        return self.top.data

    def size(self):
        count = 0
        curr = self.top

        while curr:
            count += 1
            curr = curr.next

        return count