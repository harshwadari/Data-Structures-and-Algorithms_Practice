# 143. Reorder List
"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Better approach using extra space 
# TC = O(N) and SC = O(N)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        node = []
        curr = head
        while curr is not None:
            node.append(curr)
            curr = curr.next
        left = 0
        right = len(node) - 1
        while left < right:
            node[left].next = node[right]
            if left + 1 == right:
                break
            node[right].next = node[left + 1]
            left += 1
            right -= 1
        node[right].next = None



# Optimal Appraoch using finding middle first reversing full after middle merging first half and second half alternatively
# TC = O(N) and SC = O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second != None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first = head
        second = prev
        while second != None:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext