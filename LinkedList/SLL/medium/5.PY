# find the length of loop in linked list

# brute using hasmap
# TC = O(N) and SC = O(N)
def loop(self,head):
    temp = head
    mapi = {}
    counter  = 0
    while temp is not None:
        if temp in mapi:
            length_loop = counter - mapi[temp]
            return length_loop
        mapi[temp] = counter
        counter +=1
        temp = temp.next
    return 0


# optimal approach using slow and fast pointer
# TC = O(N) and SC = O(1)
def looplength(self,head):
    slow = head
    fast = head
    counter = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        counter +=1
        fast = fast.next.next
        if slow == fast:
            return counter
    return 0
