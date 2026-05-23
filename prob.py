# swap adjacent nodes of singly linked list
# optimal approach using 3 pointers
# TC = O(N) and SC = O(1)
def swapPairs(head):
    if head is None or head.next is None:
        return head
    temp = head
    prev = None
    newHead = head.next
    while temp is not None and temp.next is not None:
        front = temp.next
        back = front.next
        front.next = temp
        temp.next = back
        if prev is not None:
            prev.next = front
        prev = temp
        temp = back
    return newHead