class kQueues:
    def __init__(self, n, k):
        self.ans=[[] for _ in range(k)]
        self.size=0
        self.n=n

    def enqueue(self, x, i):
        self.ans[i].append(x)
        self.size+=1

    def dequeue(self, i):
        if self.ans[i]:
            self.size-=1
            return self.ans[i].pop(0)
        else:
            return -1
        

    def isEmpty(self, i):
        if len(self.ans[i])==0:
            return True
        return False
        
        
    def isFull(self):
        if self.size==self.n:
            return True
        return False