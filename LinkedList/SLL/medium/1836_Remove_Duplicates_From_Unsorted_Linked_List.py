# 1836 Remove Duplicates From a unsorted Linked List
"""
Given the head of a linked list, find all the values that appear more than once in 
the list and delete the nodes that have any of those values.

Return the linked list after the deletions.

Example 1:
Input: head = [1,2,3,2]

Output: [1,3]

Explanation: 2 appears twice in the linked list, so all 2's should be deleted. 
After deleting all 2's, we are left with [1,3].

Example 2:
Input: head = [2,1,1,2]

Output: []

Explanation: 2 and 1 both appear twice. All the elements should be deleted.



Constraints:
The number of nodes in the list is in the range [1, 105]
1 <= Node.val <= 105
"""

# Optimal Appraoch using hashmap
# TC = O(N) and SC = O(N)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # Your code goes here
        temp = head
        freq = {}
        while temp != None:
            if temp.val in freq:
                freq[temp.val] += 1
            else:
                freq[temp.val] = 1
            temp = temp.next
        dummyNode = ListNode(0)
        dummyNode.next = head
        prev = dummyNode
        temp = head
        while temp != None:
            if freq[temp.val] > 1:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return dummyNode.next
