# reverse a doubly linked list


# brute force approach using stack
# TC = O(2N) and SC = O(N)
def reverseDLL(head):
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        e = stack.pop()
        temp.val = e
        temp = temp.next
    return head


# optimal approach using 3 pointers
# TC = O(N) and SC = O(1)
def revDLL(head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next = prev
        temp.prev = front
        prev = temp
        temp = front
    return prev