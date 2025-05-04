class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        idx=[0]
        return self.trav(idx,0,size-1,pre,preMirror,size)
        
    
    def trav(self,idx,start,end,pre,preMirror,n):
        if idx[0]>=n or start>end:return None
        
        if idx[0]==n-1 or start==end:
            temp=Node(pre[idx[0]])
            idx[0]+=1
            return temp
        
        temp=Node(pre[idx[0]])
        idx[0]+=1
        for i in range(start,end+1):
            if pre[idx[0]]==preMirror[i]:
                temp.left=self.trav(idx,i,end,pre,preMirror,n)
                temp.right=self.trav(idx,start+1,i-1,pre,preMirror,n)
                break
        return temp