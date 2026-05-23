# TC = O(1) and SC = O(N)

from collections import deque
class StackusingQueue:
    def __init__(self):
        self.queue = deque([])
    def push(self,x):
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
             self.queue.append(self.queue.popleft())
    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()
    def isempty(self):
        return len(self.queue) == 0
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
    def sixe(self):
        return len(self.queue)