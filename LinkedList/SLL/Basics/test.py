class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def appendatEnd(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# -------- Driver Code --------
if __name__ == "__main__":
    ll = SinglyLinkedList()
    n = int(input())   # number of elements
    for _ in range(n):
        val = int(input())
        ll.appendatEnd(val)

    ll.display()