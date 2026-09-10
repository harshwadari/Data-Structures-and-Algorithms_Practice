# 82. Remove Duplicates from Sorted List II
"""
You are given the head of a sorted linked list.

Delete all nodes that have duplicate numbers, leaving only distinct numbers 
from the original list.

Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# NoobMaster Way using array and doing ops
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head ) :
        result = []
        freq = {}
        result1 = []
        temp = head
        while temp is not None:
            result.append(temp.val)
            temp = temp.next
        for num in result:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key,value in freq.items():
            if value < 2:
                result1.append(key)
            else:
                continue
        dummy = ListNode(0)
        temp = dummy
        for i in range(len(result1)):
            temp.next = ListNode(result1[i])
            temp = temp.next
        return dummy.next



# Optimal Appraoch using linked list two pointers
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
        dummyNode = ListNode(0)
        prev = dummyNode
        dummyNode.next = head
        curr = head
        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummyNode.next