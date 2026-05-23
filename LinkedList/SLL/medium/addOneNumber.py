# Add one number to linked list 
"""
Intuition

Think like how you add 1 on paper.

Example:

129 + 1

You start from the last digit.

Cases:

Last digit < 9
Just add 1 and stop.

1 → 2 → 3
becomes
1 → 2 → 4

Last digit = 9
It becomes 0 and carry goes left.

1 → 2 → 9
becomes
1 → 3 → 0

All digits = 9

9 → 9 → 9
becomes
1 → 0 → 0 → 0

The difficulty is linked list cannot move backward.

So we need tricks.
"""



# Brute Force Approach
# Idea

# Convert linked list → number

# Add 1

# Convert back to linked list


# TC = O(N) and SC = O(1)
class Node:
    def __init__(self,val):
        self.val = val
def addonenumber(self,head):
    num = 0
    temp = head
    while temp is not None:
        num = num*10 + temp.val
        temp = temp.next
    num +=1

    # back to linkedlist
    s = str(num)
    dummynode = Node(0)
    currNode = dummynode

    for char in s:
        currNode.next = Node(int(char))
        currNode =  currNode.next
    return dummynode.next
"""
Problem
Integer overflow if list is huge
Not preferred in interviews
"""


# optimal appraoch using recursion 

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def helper(self,node):
        if node is None:
            return 1
        carry = self.helper(node.next)
        node.data += carry
        if node.data < 10:
            return 0
        node.data = 0
        return 1
        
    def addOne(self,head):
        #Returns new head of linked List.\
        carry = self.helper(head)
        if carry :
            newNode = Node(1)
            newNode.next = head
            head = newNode
        return head
     