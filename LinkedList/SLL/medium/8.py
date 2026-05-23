# 19. Remove Nth Node From End of List


"""
Docstring for LinkedList.SLL.medium.8

Given the head of a linked list, remove the nth 
node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
"""


# brute force 
# TC = O(2N) and SC = O(1)
def removenthNode(self,head,n):
    temp = head
    length = 0
    while temp is not None:
        temp = temp.next
        length +=1
    
    if length == n:
        new_node = head.next
        return new_node
    pos = length -n
    temp = head
    count = 1
    while count < pos:
        temp = temp.next
        count +=1
    temp.next = temp.next.next
    return head



# optimal appraoch
# TC = O(N) and SC = O(1)

def remove(self,head,n):
     
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next  = slow.next.next
        return head