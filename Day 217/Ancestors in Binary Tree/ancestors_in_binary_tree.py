from collections import deque
class Solution:

    def Ancestors(self, root, target):
        
        if root.data==target:return []
        ans=[]
        q=deque()
        q.append((root,[]))
        while q:
            node,ancestor=q.popleft()
            if node.data==target:return ancestor
            if node.left:q.append((node.left,[node.data]+ancestor))
            if node.right:q.append((node.right,[node.data]+ancestor))
        return ans