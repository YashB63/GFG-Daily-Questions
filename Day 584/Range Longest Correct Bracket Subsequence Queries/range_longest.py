class Solution:
    def merge(self,lchild,rchild):
        pnode=node()
        
        minmatch=min(lchild.op,rchild.cl)
        
        pnode.pair = lchild.pair + rchild.pair + minmatch
        pnode.op = lchild.op + rchild.op - minmatch
        pnode.cl = lchild.cl + rchild.cl - minmatch
        
        return pnode
    
    def gls(self,st,n,qs,qe,ss,se,si):
        if ss>qe or se<qs:
            return node()
        
        if ss>=qs and se<=qe:
            return st[si]
        
        mid=ss+(se-ss)//2
        left=self.gls(st,n,qs,qe,ss,mid,si*2+1)
        right=self.gls(st,n,qs,qe,mid+1,se,si*2+2)
        
        n=self.merge(left,right)
        
        return n
        
    def getLongestSequence(self,st,n,qs,qe):
        n=self.gls(st,n,qs,qe,0,n-1,0)
        return (2*n.pair)