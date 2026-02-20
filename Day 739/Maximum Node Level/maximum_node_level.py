class Solution:
    def maxNodeLevel(self,root):
        if not root:
            return 0
        q=deque([root])
        l=1
        m=0
        mlev=0
        lev=0
        while len(q)>0:
            l=len(q)
            if l>m:
                m=l
                mlev=lev
            while l>0:
                Node=q.popleft()
                if Node.left:
                    q.append(Node.left)
                if Node.right:
                    q.append(Node.right)
                l-=1
            lev=lev+1
        return mlev