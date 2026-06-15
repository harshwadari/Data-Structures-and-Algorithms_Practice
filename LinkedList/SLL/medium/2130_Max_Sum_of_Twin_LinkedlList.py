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