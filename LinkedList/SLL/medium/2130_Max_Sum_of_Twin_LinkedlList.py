# 2130. Maximum Twin Sum of a Linked List

# TC = O(2N) and SC = O(N)
def pairSum(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: int
    """
    stack = []
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    ans = 0
    while slow is not None:
        ans = max(ans,slow.val + stack.pop())
        slow = slow.next
    return ans       




# Using array Appraoch 
# TC = O(2N) and SC = O(N)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        result = []
        temp = head
        total = 0
        ans = 0
        while temp is not None:
            result.append(temp.val)
            temp = temp.next
        n = len(result)
        for i in range(len(result)):
            total = result[i] + result[n - 1 - i]
            ans = max(ans,total)
        return ans



# Optimal Approach 
# TC = O(3N) and SC = O(1)

def twinSumLinkedList(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next
    prev = None
    curr = slow
    while curr != None:
        nodenext = curr.next
        curr.next = prev
        prev = curr
        curr = nodenext
    first = head
    second = prev
    ans = 0
    while second != None:
        total = first.val + second.val
        ans = max(ans,total)
        first = first.next
        second = second.next
    return ans 