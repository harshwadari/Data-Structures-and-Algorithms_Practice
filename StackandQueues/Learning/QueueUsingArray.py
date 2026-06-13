# Queue Using Array 

# TC = O(1) and SC = O(N)

class Queue:
    def __init__(self):
        self.x = []
    def enqueue(self,value):
        self.x.append(value)
    def dequeue(self):
        if len(self.x) == 0:
            return None
        return self.x.pop(0)
    def rear(self):
        if len(self.x) == 0:
            return None
        return self.x[-1]
    def front(self):
        if len(self.x) == 0:
            return None
        return self.x[0]
    def size(self):
        return len(self.x) 
    

# ---- Testing ----
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.front())   # 1
print(queue.rear())    # 5
print(queue.size())    # 5