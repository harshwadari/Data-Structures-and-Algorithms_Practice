# 2095. Delete the Middle Node of a Linked List

"""
Docstring for LinkedList.SLL.medium.9

You are given the head of a linked list. Delete the middle 
node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th 
node from the start using 0-based indexing, where ⌊x⌋ denotes 

the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.
"""



# brute force appraoch
# TC = O(N+N/2) and SC = O(1)

def deletemiddle(self,head):
    if not head or not head.next:
        return None
    temp = head
    length = 0
    while temp != None:
        temp = temp.next
        length +=1
    temp = head
    for _ in range(1,length//2):
        temp = temp.next
        if temp.next:
            middle = temp.next
        temp.next = temp.next.next
    return head


# optimal

def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
