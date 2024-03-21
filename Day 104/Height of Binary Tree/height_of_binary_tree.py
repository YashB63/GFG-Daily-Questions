class Solution:
    
    def height(self, root):
        
        if root is None:
            return 0
        else:
            l = self.height(root.left)
            r = self.height(root.right)
        return max(l+1 , r+1)