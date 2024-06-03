import sys
sys.setrecursionlimit(50000)

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    
    def connect(self, root):
        if not root:
            return root
        s=[root]
        while s:
            prev=None
            n=len(s)
            for i in range(n):
                curr=s.pop(0)
                if prev is not None:
                    prev.nextRight=curr
                prev=curr
                if curr.left:
                    s.append(curr.left)
                if curr.right:
                    s.append(curr.right)
                
            prev=None
        return root