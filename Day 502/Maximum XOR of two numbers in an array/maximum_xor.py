class Node:
    def __init__(self):
        self.store = [None]*2
    
    def insert(self, value):
        for i in range(30, -1, -1):
            mask = (1<<i)
            bit = int(value & mask != 0)
            if self.store[bit] is None:
                self.store[bit] = Node()
            self = self.store[bit]
        
    def query_max_xor(self, n):
        ret = 0
        for i in range(30, -1, -1):
            mask = (1<<i)
            bit = int(n & mask != 0)
            other = 1-bit
            if self.store[other]:
                ret |= (1<<i)
                self = self.store[other]
            else:
                self = self.store[bit]
        return ret
    
    
class Solution:
    def maxXor(self, arr):
        tri = Node()
        for n in arr:
            tri.insert(n)
            
        ans = 0
        for n in arr:
            ans = max(ans, tri.query_max_xor(n))
        return ans