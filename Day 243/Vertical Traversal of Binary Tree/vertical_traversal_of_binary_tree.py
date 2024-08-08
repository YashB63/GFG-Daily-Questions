from collections import defaultdict

class Solution:
    
    def verticalOrder(self, root): 
        idx = defaultdict(list)
        
        q = deque([(0, root)])
        
        while q:
            e, cn = q.popleft()
            
            idx[e].append(cn.data)
            
            if cn.left:
                q.append((e-1, cn.left))
            
            if cn.right:
                q.append((e+1, cn.right))
            
        mn, mx = min(idx.keys()), max(idx.keys())

        res = []
        
        for e in range(mn, mx+1):
            res += idx[e]
            
        return res