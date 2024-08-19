class MyStack:
    top=None    
    
    def push(self, data):
        if(self.top==None):
            self.top=StackNode(data)
        else:
            newNode=StackNode(data)
            newNode.next=self.top
            self.top=newNode
            
    def pop(self):
        if(self.top==None):
            return -1
        topNodedata=self.top.data
        self.top=self.top.next
        return topNodedata