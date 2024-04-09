class Solution:
    
    def KDistance(self,root,k):
    
        q=[root]
        c=0
        while(q):
            l=len(q)
            t=[]
            while(l>0):
                n=q[0]
                q.remove(n)
                t.append(n.data)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            if c==k:
                return t
            c+=1
        return []