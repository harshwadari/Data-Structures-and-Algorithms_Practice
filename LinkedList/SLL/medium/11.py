# Sort a Linked List of 0's 1's and 2's
'''
Given the head of a singly linked list consisting of only 0, 1 or 2.
Sort the given linked list and return the head of the modified list.
Do it in-place by changing the links between the nodes without creating new nodes.



Example 1

Input: linkedList = [1, 0, 2, 0 , 1]

Output: [0, 0, 1, 1, 2]

Explanation: The values after sorting are [0, 0, 1, 1, 2].'
'''
# brute force 
# TC = O(N) and SC = O(N)
def sort012(self,head):
    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
        arr.sort()
    temp = head
    for val in arr:
        temp.data =val
        temp = temp.next
    return head



# optimal appraoch 
# TC = O(2N) and SC = O(1)
def sorting012(self,head):
    count1 = 0
    count2 = 0
    count3 = 0
    temp = head
    while temp is not None:
        if temp.val == 0:
            count1 +=1
        elif temp.val == 1:
            count2 +=1
        else:
            count3 +=1
        temp = temp.next
    temp = head
    while temp is not None:
        if count1 > 0:
            temp.val = 0
            count1 -=1
        elif count2 > 0:
            temp.val  = 1
            count2 -=1
        elif count3 > 0:
            temp.val = 2
            count3 -=1
        temp = temp.next
    return head



# more optimal using 


"""
def sort(self,head):
    if not head or not head.next:
        return head

      zeroHead = ListNode(-1)
      oneHead = ListNode(-1)
      twoHead = ListNode(-1)

      zero = zeroHead
      one = oneHead
      two = twoHead

      while temp is not None:
        if temp.data == 0:
          zero.next = temp
          zero = temp
        elif temp.data == 1:
          one.next = temp
          one = temp
        elif temp.data == 2:
          two.next = temp
          two = temp
        temp = temp.next

        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
        newHead = zeroHead.next
        return newHead 


"""