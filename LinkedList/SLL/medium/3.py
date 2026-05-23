# Linked list cycle detection  141

"""
Docstring for LinkedList.SLL.medium.3

Given head, the head of a linked list, determine if the linked list
has a cycle in it.
There is a cycle in a linked list if there is some node in the 
list that can be reached again by continuously following the ne
xt pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos i
s not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail
connects to the 1st node (0-indexed).
"""



# brute force using hasmpa
# TC = O(N) and SC = O(N)

def detectcycle(self,head):
    
    temp = head
    my_set = set()
    while temp is not None:
        if temp in my_set:
            return True
        my_set.add(temp)
        temp = temp.next
    return False



# optimal approach using slow fast pointer floyd cycle detection
# TC = O(N) and SC = O(1)

def detectllcycle(self,head):
    temp = head
    slow = head
    fast = head
    while temp is not None and temp.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False