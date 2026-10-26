# 86. Partition List
"""
Given the head of a linked list and a value x, partition it such that all 
\nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each 
of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""



# Array appraoch 
# TC = O(3N) and SC = O(3N)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        result = []
        temp = head
        while temp is not None:
            result.append(temp.val)
            temp = temp.next
        ans = []
        ans2 = []
        for i in range(len(result)):
            if result[i] < x:
                ans.append(result[i])
            else:
                ans2.append(result[i])
        ans3 = ans + ans2
        dummy = ListNode(0)
        temp = dummy
        for i in range(len(ans3)):
            temp.next = ListNode(ans3[i])
            temp = temp.next
        return dummy.next



#Optimal Appraoch 
"""
The idea is to create two separate linked lists using the existing nodes, then connect them.
- before: stores nodes with values less than x.
- after: stores nodes with values greater than or equal to x.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC = O(N) and SC = O(N)
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        list1 = ListNode(0)
        list2 = ListNode(0)
        p1 = list1
        p2 = list2
        temp = head
        while temp != None:
            if temp.val < x:
                p1.next = temp
                p1 = p1.next
            else:
                p2.next = temp
                p2 = p2.next
            temp = temp.next
        p2.next = None
        p1.next = list2.next
        return list1.next