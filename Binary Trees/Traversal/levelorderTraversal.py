# level order traversal ( bread first Search)
from collections import deque
# TC = O(N) and SC = O(N)
def levelorder(self,root):
    if not root:
        return []
    queue = deque([])
    result = []
    queue.append(root)
    while queue:
        level = []
        for _ in range(len(queue)):
            e = queue.popleft()
            level.append(e.val)
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
        result.append(level)
    return result