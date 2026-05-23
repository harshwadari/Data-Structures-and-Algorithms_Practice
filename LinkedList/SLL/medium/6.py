# 234. Palindrome Linked List

"""
Docstring for LinkedList.SLL.medium.6

Given the head of a singly linked list, return 
true if it is a palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true

"""

# brute force using stack
# TC = O(2N) and SC = O(N)
def palindrome(self,head):
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        e = stack.pop()
        if temp.val != e:
            return False
        temp = temp.next
    return True



# otimal using two fast and slow pointer
# TC = O(3N) and SC = (1)
def palindromell(self,head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    prev = None
    curr = slow
    while curr is not None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front
    left = head
    right = front
    while right is not None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True