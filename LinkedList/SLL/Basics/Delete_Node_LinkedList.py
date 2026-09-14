# delete node from linked list 

"""
Docstring for LinkedList.2


"""


# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteHead(self, head):
        if head is None or head.next is None:
            return None
        head = head.next
        return head
    
    def deletenode(self,node):
        node.val = node.next.val
        node.next = node.next.next




# delete node in a linked list of a speficic position 
# TC = O(N) and SC = O(1)
''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if head == None:
            return head
        if x == 1:
            return head.next
        curr = head
        for i in range(x - 2):
            curr = curr.next
        curr.next = curr.next.next
        return head