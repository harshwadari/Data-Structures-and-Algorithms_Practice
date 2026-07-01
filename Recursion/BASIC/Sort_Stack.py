# Sort a Stack using recursion 

# brute appraoch 
def sortStack(st):
    return st.sort(reverse=False)


# different approach using recursion

def insertSorted(stack, value):

    # Insert when stack is empty or current top is smaller/equal
    if not stack or stack[-1] <= value:
        stack.append(value)
        return

    top = stack.pop()

    insertSorted(stack, value)

    stack.append(top)


def sortStack(stack):

    if not stack:
        return

    top = stack.pop()

    sortStack(stack)

    insertSorted(stack, top)


stack = [3, 1, 4, 2]

sortStack(stack)

print(stack)