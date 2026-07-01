# Reverse a Stack using Recursion

# brute appraoch using sort function
# TC = O(NlogN) and SC = O(1)

def revstack(arr):
    return arr.reverse()


# using recursion
def insertAtBottom(stack, value):

    if not stack:
        stack.append(value)
        return

    top = stack.pop()

    insertAtBottom(stack, value)

    stack.append(top)


def reverseStack(stack):

    if not stack:
        return

    top = stack.pop()

    reverseStack(stack)

    insertAtBottom(stack, top)


stack = [1, 2, 3, 4]

reverseStack(stack)

print(stack)