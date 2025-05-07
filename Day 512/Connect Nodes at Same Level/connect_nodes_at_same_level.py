class Solution:
    def connect(self, root):
        if not root:
            return None
        from collections import deque
        queue=deque([root])
        while queue:
            prev=None
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.nextRight=node
                prev=node 
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            prev.nextRight=None        
            
        return root