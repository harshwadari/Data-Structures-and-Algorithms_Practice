# Introduction to doubly Linked list 
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
        
    def insertAtHead(self,val): # TC = O(1) and SC = O(1)
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def insertAtTail(self,val): # TC = O(N) and SC = O(1)
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
    def insertAtPos(self,pos,val): # TC = O(N) and SC = O(1)
        newNode = Node(val)
        if pos == 1:
            self.insertAtHead(val)
            return
        temp = self.head
        for _ in range(1,pos-1):
            temp = temp.next
        if temp.next is None:
            self.insertAtTail(val)
            return
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        newNode.prev = temp
    def deleteAtHead(self): # TC = O(1) and SC = O(1)
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        temp.next = None
    