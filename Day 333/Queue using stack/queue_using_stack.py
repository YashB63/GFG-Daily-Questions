class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self,X):
        self.s1.append(X)
        
    def dequeue(self):
        if not self.s2:
           while self.s1:
              self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
        else:
            return -1