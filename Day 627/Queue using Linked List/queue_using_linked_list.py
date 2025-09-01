class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def push(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp
        
    def pop(self):
        if self.isEmpty():
            return -1

        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

        return str(temp.data)