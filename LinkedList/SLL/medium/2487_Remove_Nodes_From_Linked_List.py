# 2487. Remove Nodes From Linked List
"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the 
right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""

# Better Approach using Monotonic stack 
# TC = (2N) and SC = O(N)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        temp = head
        while temp is not None:
            while len(stack) != 0 and temp.val > stack[-1]:
                stack.pop()
            stack.append(temp.val)
            temp = temp.nextA
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(stack)):
            curr.next = ListNode(stack[i])
            curr = curr.next
        return dummy.next



# Optimal Appraoch using reverse linked list 
# TC = O(2N) and SC = O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            prev = None
            curr = head
            while curr != None:
                front =  curr.next
                curr.next = prev
                prev = curr
                curr = front
            return prev
        head = reverse(head)
        curr = head
        currMax = curr.val
        while curr.next != None:
            if curr.next.val < currMax:
                curr.next = curr.next.next
            else:
                currMax = curr.next.val
                curr = curr.next
        return reverse(head)