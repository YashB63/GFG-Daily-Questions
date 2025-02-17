class Solution:
    def ladoos(self, root, src, k):
        ans_set=set()
        def fun1(root,k):
            if k==-1:
                return
            ans_set.add(root)
            if root.left!=None:
                fun1(root.left,k-1)
            if root.right!=None:
                fun1(root.right,k-1)
            
        def fun(root,src,k):
            if root==None:
                return -1
            if root.data==src:
                fun1(root,k)
                return k-1
            temp=fun(root.left,src,k)
            if temp!=-1:
                fun1(root,temp)
                return temp-1
            temp=fun(root.right,src,k)
            if temp!=-1:
                fun1(root,temp)
                return temp-1
            
            return -1
            
        fun(root,src,k)    
            
        ans=0
        
        for value in ans_set:
            ans+=value.data
        return ans