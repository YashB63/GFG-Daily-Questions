class Solution:
    
    def levelOrder(self,root):
        
        res=[]
        q=deque([root])
        while q:
            
            temp =q.popleft()
            res.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return res