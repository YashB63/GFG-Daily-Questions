class Solution:
    
    def getMaxWidth(self,root):
       
        if root is None:
            return 0
            
        q = deque()
        res =0
        
        q.append(root)
        
        while q:
            c = len(q)
            for i in range(c):
                curr =q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res = max(res,c)
        return res