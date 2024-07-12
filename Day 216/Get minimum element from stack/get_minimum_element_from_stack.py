class stack:
    def __init__(self):
        self.s=[]
        self.ss=[]

    def push(self,x):
        
        self.s.append(x)
        if not self.ss or self.ss[-1]>=x:
            self.ss.append(x)
            
    def pop(self):
        
        if not self.s:
            return -1
        ans=self.s.pop()
        if self.ss[-1]==ans:
            self.ss.pop()
        return ans

    def getMin(self):
        
        if not self.ss:
            return -1
        return self.ss[-1]