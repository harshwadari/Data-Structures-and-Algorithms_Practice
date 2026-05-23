# Removes duplicates from a sorted doubly linked list
# optimal approach using 2 pointers
# TC = O(N) and SC = O(1)
def removeDuplicates(head):
    if head is None or head.next is None:
        return head
    temp = head
    while temp is not None and temp.next is not None:
        if temp.val == temp.next.val:
            next_node = temp.next
            temp.next = next_node.next
            if next_node.next is not None:
                next_node.next.prev = temp
            next_node.prev = None
            next_node.next = None
        else:
            temp = temp.next
    return head