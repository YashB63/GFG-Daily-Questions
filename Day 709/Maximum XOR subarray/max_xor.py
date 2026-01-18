class Node:
    def __init__(self):

        self.data = 0
        self.left = None  
        self.right = None  

class Solution:

    def __init__(self):

        self.root = Node()

    def insert(self, pre_xor):
        self.temp = self.root
        
        for i in range(31, -1, -1):
            val = pre_xor & (1 << i)

            if val:
                if not self.temp.right:
                    self.temp.right = Node()
                self.temp = self.temp.right

            if not val:
                if not self.temp.left:
                    self.temp.left = Node()
                self.temp = self.temp.left
        self.temp.data = pre_xor

    def query(self, xor):

        self.temp = self.root

        for i in range(31, -1, -1):
            val = xor & (1 << i)

            if val:
                if self.temp.left:
                    self.temp = self.temp.left
                elif self.temp.right:
                    self.temp = self.temp.right
            else:
                if self.temp.right:
                    self.temp = self.temp.right
                elif self.temp.left:
                    self.temp = self.temp.left

        return xor ^ self.temp.data

    def maxSubarrayXOR(self, n, Arr):
        self.insert(0)
        result = 0
        pre_xor = 0
        
        for i in range(n):
            pre_xor = pre_xor ^ Arr[i]
            self.insert(pre_xor)
            result = max(result, self.query(pre_xor))
            
        return result