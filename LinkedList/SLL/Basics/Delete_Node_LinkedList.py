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