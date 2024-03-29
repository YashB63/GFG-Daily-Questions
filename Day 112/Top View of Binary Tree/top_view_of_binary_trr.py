class Solution:
    
    def topView(self,root):
        
        if root is None:
            return []

        top_view = {}
        queue = deque([(root, 0)]) 
        
        while queue:
            node, hd = queue.popleft()
            if hd not in top_view:
                top_view[hd] = node.data 
            if node.left:
                queue.append((node.left, hd - 1)) 
            if node.right:
                queue.append((node.right, hd + 1)) 
       
        sorted_keys = sorted(top_view.keys())
        return [top_view[key] for key in sorted_keys]