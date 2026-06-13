"""
Stack Data Structure 

Stack is linear data structure where you can store any type of data like int, string, float etc 
It uses LIFO (Last In First Out) 
Stack has four functions 1.Pop() 
2.Push(x) where x is element to add in stack 
3.top() returns the top most element of stack 
4.size() returns the size of stack 

"""
# TC = O(1) and SC = O(N)
class Stack:
    def __init__(self):
        self.x = []
    def push(self,value):
        self.x.append(value)
    def pop(self):
        if len(self.x) == 0:
            return None
        return self.x.pop()
    def top(self):
        if len(self.x) == 0:
            return None
        return self.x[-1]
    def isempty(self):
        return len(self.x) == 0

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)
print(stack.top())
print(stack.pop())
print(stack.top())