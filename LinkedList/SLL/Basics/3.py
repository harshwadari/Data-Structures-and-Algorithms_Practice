# to check the lenght of linked list by traversing it 


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def length(self,head):
        count = 0
        temp = head
        while temp is not None:
            count+=1
            temp = temp.next
        return count