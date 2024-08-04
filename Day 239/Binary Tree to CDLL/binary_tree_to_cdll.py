class Solution:
    
    def bTreeToClist(self, root):
        from collections import deque
        q = deque()
        def order(root):
            if not root:
                return
            order(root.left)
            q.append(root)
            order(root.right)
            return
        order(root)
        
        root = q[0]
        prev = q[0]
        while q:
            node = q.pop()
            node.right = prev
            prev.left = node
            prev = node
        return root