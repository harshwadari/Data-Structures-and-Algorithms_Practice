# Remove Duplicates from Linked List
"""
Given a head of an unsorted linked list. Remove duplicate elements from this 
unsorted Linked List. When a value appears in multiple nodes, the node which 
appeared first should be kept, all other duplicates are to be removed.

Examples:

Input: head = 5 -> 2 -> 2 -> 4
Output: 5 -> 2 -> 4
Explanation: Given linked list elements are 5 -> 2 -> 2 -> 4, in which 2 is 
repeated only. So, we will delete the extra repeated elements 2 from the linked 
list and the resultant linked list will contain 5->2->4
 
Input: head = 2 -> 2 -> 2 -> 2 -> 2
Output: 2
Explanation: Given linked list elements are 2 -> 2 -> 2 -> 2 -> 2, in which 2 is 
repeated. So, we will delete the extra repeated elements 2 from the linked list 
and the resultant linked list will contain only 2.

Constraints:

1 ≤ size of linked list ≤ 106
0 ≤ node.data ≤ 106

"""

# Hashset approach 
# TC = O(N) and SC = O(N)
''' Structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def removeDuplicates(self, head):
        # code here
        seen = set()
        curr = head
        prev = None
        while curr != None:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr = curr.next
        return head



# Two pointer appraoch without extra space 
# TC = O(N ^2) and SC = O(1)
def removeDuplicates(head):
    curr = head

    while curr != None:
        runner = curr

        while runner.next != None:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        curr = curr.next

    return head