from queue import Queue

class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    def maxDepth(self, root):
        count=0
        q=Queue()
        q.put(root)
        count=0
        while not q.empty():
            temp=[]
            for i in range(q.qsize()):
                node=q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            count+=1
        return count