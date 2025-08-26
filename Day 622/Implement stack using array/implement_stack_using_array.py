class MyStack:
    def __init__(self):
        self.arr = [-1] * 100
        self.top = -1

    def push(self, x):
        if self.top < 99:  
            self.top += 1
            self.arr[self.top] = x  

    def pop(self):
        if self.top == -1:
            return -1
        val = self.arr[self.top]  
        self.top -= 1  
        return val