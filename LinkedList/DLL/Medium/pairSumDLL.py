# Pair sum in Doubly Linked List

# brute force approach is to use two loops and check for each pair 
# if their sum is equal to the given sum or not. TC = O(N^2) and SC = O(1)
# TC = O(N^2) and SC = O(1)
def pairSum(head, target):
    temp1 = head
    result = []
    while temp1 is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.val + temp2.val == target:
                result.append((temp1.val, temp2.val))
            temp2 = temp2.next
        temp1 = temp1.next
    return result

# better approach using set
# TC = O(N) and SC = O(N)
def pairSumSet(head, target):
    seen = set()
    result = []
    temp = head
    while temp is not None:
        remaining = target - temp.val
        if remaining in seen:
            result.append((remaining, temp.val))
        seen.add(temp.val)
        temp = temp.next
    return result

# optimal approach using two pointers
# TC = O(N) and SC = O(1)
def pairSumTwoPointers(head, target):
    left = head
    result  = []
    right = head
    while right.next is not None:
        right = right.next
    while left is not None and right is not None and left.val < right.val:
        total = left.val + right.val
        if total == target:
            result.append((left.val, right.val))
            left = left.next
            right = right.prev
        elif total > target:
            right = right.prev
        else:
            left = left.next
    return result