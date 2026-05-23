# 148. Sort List

"""
Docstring for LinkedList.SLL.medium.10

Given the head of a linked list, return the 
list after sorting it in ascending order.

Input: head = [4,2,1,3]
Output: [1,2,3,4] 
"""


# brute force appraoch
# TC = O(2N+ NlogN) and SC = O(N)
def sortList(self,head):
    temp = head
    arr = []
    while temp != None:
        arr.append(temp.val)
        temp = temp.next
    arr.sort()
    temp = head
    for val in arr:
        temp.val = val
        temp = temp.next
    return head



# otpimal method 
def sortll(self,head):
    if not head or not head.next:
        return head
    