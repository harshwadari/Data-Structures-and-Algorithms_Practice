# reverse the linked list 
"""
Docstring for LinkedList.SLL.medium.2

Given the head of a singly linked list, reverse
the list, and return the reversed list.


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# extreme naive appraoch 
"""
first we will traverse linked list and put all values inside a array 
then reverse arrray and again travese array and put all reverse data inside linked list 
"""
# TC = O(3N) and SC = O(N)
def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        temp = head
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        left = 0
        right = len(arr) - 1
        while left <= right:
            arr[left] , arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        temp = head
        for i in range(len(arr)):
            temp.val = arr[i]
            temp = temp.next
        return head





# brurte force approach
# TC = O(2N) and SC = (N)
def reverse(self,head):
    stack = []
    temp = head
    while temp is not  None:
        stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        e = stack.pop()
        temp.val = e
        temp = temp.next
    return head


#optimal method using 3 pointers
# TC = O(N) and SC = O(1)
def reversell(self,head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev


# recursive appraoch 

def revll(self,head):
    if head is None or head.next is None:
        return head
    new_node = self.revll(head.next)
    head.next.next = head
    head.next = None
    return new_node

