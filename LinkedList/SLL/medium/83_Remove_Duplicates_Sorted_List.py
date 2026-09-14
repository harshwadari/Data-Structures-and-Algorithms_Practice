# 83. Remove Duplicates from Sorted List
"""
Given the head of a sorted linked list, delete all duplicates such that
 each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Optimal Appraoch using two pointer 
# TC = O(N) and SC = O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        slow = head
        fast = head.next
        while fast is not None:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return head



"""
"I'm modifying the next pointers in-place, so I don't create another list or additional nodes. 
The removed nodes become unreachable and can be reclaimed by Python's garbage collector."
"""


