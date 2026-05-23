# to find the middle of a linked list

"""
Docstring for LinkedList.SLL.medium.1

Given the head of a singly Linked List,
return the middle node of the Linked List.
If the Linked List has an even number of nodes, 
return the second middle one.


Example 1

Input: head -> 3 -> 8 -> 7 -> 1 -> 3

Output(value at returned node): 7

Explanation: There are 5 nodes, so the middle node is the 3rd Node, with value 7.

"""


# brute force method 
# TC = O(N) and Sc = O(1)
def middle(self,head):
    count = 0
    temp = head
    while temp is not None:
        temp = temp.next
        coutn +=1
    temp = head
    for i in range(count//2):
        temp = temp.next
    return temp



# optimal using slow and fast pointer
# TC = O(N) and SC = O(1)

def middile(self,head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow