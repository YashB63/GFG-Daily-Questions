class Solution:
    def findMax(self,root):
        if(root==None):
            return -1000000
        return max(root.data,self.findMax(root.left),self.findMax(root.right))
    
    def findMin(self,root):
        if(root==None):
            return 1000000
        return min(root.data,self.findMin(root.left),self.findMin(root.right))