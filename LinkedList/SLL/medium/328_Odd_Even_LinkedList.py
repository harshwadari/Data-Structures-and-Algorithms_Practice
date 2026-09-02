# 328. Odd Even Linked List

"""
Docstring for LinkedList.SLL.medium.7


Given the head of a singly linked list, group all the 
nodes with odd indices together followed by the nodes with 
even indices, and return the reordered list.
The first node is considered odd, and the second node 
is even, and so on.
Note that the relative order inside both the even and odd 
groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

"""

# optimal method using two pointers
# TC = O(N) and SC = O(1)
def oddll(self,head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
        odd.next = even_head
    return head
        



# brute method using extra array space
# TC = O(N/2) and SC = O(1)
def oddEvenList(head):
    if head is None or head.next is None:
        return head

    result = []

    # odd positions
    temp = head
    while temp is not None:
        result.append(temp.val)
        if temp.next is None:
            break
        temp = temp.next.next

    # even positions
    temp = head.next
    while temp is not None:
        result.append(temp.val)
        if temp.next is None:
            break
        temp = temp.next.next

    # write back
    temp = head
    index = 0
    while temp is not None and index < len(result):
        temp.val = result[index]
        index += 1
        temp = temp.next

    return head








# using array way 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList( head ):
        arr = []
        temp = head
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        evenarr = []
        oddarr = []
        for i in range(0,len(arr),2):
            evenarr.append(arr[i])
        for i  in range(1,len(arr),2):
            oddarr.append(arr[i])
        result = evenarr + oddarr
        dummy = ListNode(0)
        temp = dummy
        for i in range(len(result)):
            temp.next = ListNode(result[i])
            temp = temp.next
        return dummy.next