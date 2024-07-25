class Solution:
    def floor(self, root, x):
        
        ans  = -1
        
        while root:
            if root.data==x:
                return x
            elif root.data<x:
                ans=max(ans, root.data)
                root = root.right
            else:
                root = root.left
        
        return ans