class Solution:
    
    def minValue(self, root):
       
        if root == None: return -1
        if root.left == None: return root.data
        
        return self.minValue(root.left)