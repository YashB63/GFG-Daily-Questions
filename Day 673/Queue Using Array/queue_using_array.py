class myQueue:
    def __init__(self, n):
        self.capacity = n
        self.arr = [0] * n
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, x):
        self.arr[self.size] = x
        self.size += 1

    def dequeue(self):
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[0]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.size - 1]