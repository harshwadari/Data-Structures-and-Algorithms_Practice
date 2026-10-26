
class Deque:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def pushFront(self, x):
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.size

        self.arr[self.front] = x
        self.count += 1
        return True

    def pushRear(self, x):
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.arr[self.rear] = x
        self.count += 1
        return True

    def popFront(self):
        if self.isEmpty():
            return -1

        x = self.arr[self.front]

        if self.count == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        self.count -= 1
        return x

    def popRear(self):
        if self.isEmpty():
            return -1

        x = self.arr[self.rear]

        if self.count == 1:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size

        self.count -= 1
        return x

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
