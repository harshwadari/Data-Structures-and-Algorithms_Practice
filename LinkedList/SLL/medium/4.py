# 142. Linked List Cycle II

"""
Docstring for LinkedList.SLL.medium.4
Given the head of a linked list, return the node where 
the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node
in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to 
denote the index of the node that tail's next pointer 
is connected to (0-indexed). It is -1 if there is no 
cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked
list, where tail connects to the second node.
"""


# Brute methode 
# TC = O(N) and SC = O(N)

def cycle(self,head):
    my_set = set()
    temp = head
    while temp is not None:
        if temp in my_set:
            return temp
        my_set.add(temp)
        temp = temp.next
    return None



# optimal method using slow fast pointer
# TC = O(N) and SC = O(1)

def cyclee(self,head):
    temp = head
    fast = head
    slow = head
    while temp is not None and temp.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
