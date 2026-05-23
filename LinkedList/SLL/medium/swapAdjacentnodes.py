# swap Adjacent node in a linked list 

# optimal approach using link manipulation
# TC = O(N) and SC = O(1)

def swapPairs(head):
    if head is None or head.next is None:
        return head
    first  = head
    second = head.next
    prev = None
    while first is not None and second is not None:
        # swap first and second
        first.next = second.next
        second.next = first
        if prev is not None:
            prev.next = second
        prev = first
        # move to next pair
        first = first.next
        if first is not None:
            second = first.next
        else:
            second = None
    return head