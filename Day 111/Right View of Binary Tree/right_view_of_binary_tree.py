class Solution:
    
    def rightView(self,root):
        
        q = deque()
        if root:
            q.append(root)
            q.append(None)
        else:
            return
        x = []
        ans = []
        while q:
            temp = q.popleft()
            if temp == None:
                ans.append(x)
                if len(q) == 0:
                    break
                x = []
                q.append(None)
            else:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                x.append(temp.data)
        arr = []
        for i in range(len(ans)):
            arr.append(ans[i][-1])
        return arr