# Queue using LinkedList
# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self, x):
        newNode = Node(x)

        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        self.count += 1

    def dequeue(self):
        if self.front is None:
            return -1

        val = self.front.data
        self.front = self.front.next
        self.count -= 1

        if self.front is None:
            self.rear = None

        return val

    def getFront(self):
        if self.front is None:
            return -1

        return self.front.data

    def size(self):
        return self.count