from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = None

class Solution:
    def createTree(self, root, l):
        que = deque([root])
        i = 0
        
        while que:
            curr = que.popleft()
            
            if (2*i + 1) < 7:
                curr.left = Node(l[2*i + 1])
                que.append(curr.left)
            
            if (2*i + 2) < 7:
                curr.right = Node(l[2*i + 2])
                que.append(curr.right)
            
            i += 1
        
        return root