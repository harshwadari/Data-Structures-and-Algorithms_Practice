# max depth of binary tree

from queue import deque
# TC = O(N) and SC = O(N)
def maxDepth(self,root):
    if root == None:
        return 0 # -1 if consider  edges as max height 
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return 1 + max(left,right)


# Iterative approach 
# TC = O(N) and SC = O(1)
def depth (root):
    queue = deque([])
    height = 0
    queue.append(root)
    while len(queue) != 0:
        level = len(queue)
        height += 1
        for _ in range(level):
            e = queue.pop()
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
    return height 