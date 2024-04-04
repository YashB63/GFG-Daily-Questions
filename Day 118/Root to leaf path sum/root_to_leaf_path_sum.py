class Solution:
    def hasPathSum(self,root, s):
        
        if root is None:
            return False
        if s <=0:
           
            return False 
        curr_sum=root.data
        
        if  root.left is None and root.right is None:
            return curr_sum==s 
        return ( self.hasPathSum(root.left,s-curr_sum) or
                 self.hasPathSum(root.right,s-curr_sum))