class Solution:
    
    def __init__(self):
        self.count=0
        
    def sumK(self,root,k):
        frq={0:1}
        def func(root,k,s,frq):
            if root==None:
                return 
            s+=root.data
            if s-k in frq :
                self.count+=frq[s-k]
            frq[s]=1+frq.get(s,0)
            func(root.left,k,s,frq)
            func(root.right,k,s,frq)
            frq[s]-=1
        func(root,k,0,frq)
        return self.count