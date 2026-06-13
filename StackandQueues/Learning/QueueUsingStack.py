# Implementation of Queue using stack
# TC = O(N) and SC = O(N)
#User function Template for python3
class StackQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, B):
        # code here
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(B)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
    def pop(self):
        # code here
        if len(self.s1) == 0:
            return -1
        return self.s1.pop()
    def peek(self):
        if len(self.s1) == 0:
            return -1
        return self.s1[-1]
    def isempty(self):
        if len(self.s1) != 0:
            return True
        return False