from collections import deque

class SpecialQueue:
    def __init__(self):
        self.q1 = deque()   
        self.q2 = deque()   
        self.q3 = deque()   

    def enqueue(self, x):
        self.q1.append(x)

        while self.q2 and self.q2[-1] > x:
            self.q2.pop()
        self.q2.append(x)

        while self.q3 and self.q3[-1] < x:
            self.q3.pop()
        self.q3.append(x)

    def dequeue(self):
        if not self.q1:
            print("Queue is empty")
            return
        frontVal = self.q1.popleft()

        if frontVal == self.q2[0]:
            self.q2.popleft()

        if frontVal == self.q3[0]:
            self.q3.popleft()

    def getFront(self):
        if not self.q1:
            print("Queue is empty")
            return -1
        return self.q1[0]

    def getMin(self):
        if not self.q1:
            print("Queue is empty")
            return -1
        return self.q2[0]

    def getMax(self):
        if not self.q1:
            print("Queue is empty")
            return -1
        return self.q3[0]