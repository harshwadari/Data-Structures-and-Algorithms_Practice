# Delete all occurrences of a given key in a doubly linked list

# optimal approach using 2 pointers
# TC = O(N) and SC = O(1)
def deleteKey(head,key):
    if head is None or (head.next is None and head.val == key):
        return None
    temp = head
    prev = None
    newHead = head
    while temp is not None:
        if temp.val == key:
            if prev is not None:
                prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev
            if temp == newHead:
                newHead = temp.next
        else:
            prev = temp
        temp = temp.next
    return newHead