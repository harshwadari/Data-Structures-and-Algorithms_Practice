# 92. Reverse Linked List II

# brute force method 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        left -=1
        right -=1
        while left < right:
            arr[left] , arr[right] = arr[right] , arr[left]
            left +=1
            right -=1
        temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            temp = temp.next
            i +=1
        return head



# optimal appraoch using three pointers
# TC = O(N) and SC = O(1)

def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        leftprev = dummyNode
        for _ in range(left - 1):
            leftprev = leftprev.next
        curr = leftprev.next
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        reverseStart = leftprev.next
        leftprev.next = prev
        reverseStart.next = curr
        return dummyNode.next

