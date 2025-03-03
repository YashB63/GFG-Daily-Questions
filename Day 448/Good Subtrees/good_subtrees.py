class Solution:
    
    def Postorder(self,root,k,count):
        if root is None:
            return set()
        lset=self.Postorder(root.left,k,count)
        rset=self.Postorder(root.right,k,count)
        
        curr_set=lset | rset | {root.data}
        if len(curr_set)<=k:
            count[0]+=1
        return curr_set
        
    def goodSubtrees(self, root, k):
        count=[0]
        st=self.Postorder(root,k,count)
        return count[0]