class Solution:
    def bottomView(self, root):
        # code here
        res = {}
        
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            if hd in res:
                res[hd].append(node.data)    
            res[hd] = [node.data]
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        return [res[i][-1] for i in sorted(res)]