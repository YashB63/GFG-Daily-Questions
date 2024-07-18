class Solution:

    def hasPathSum(self, root, target):
        
        if root is None:
            return False
        if not root.left and not root.right:
            return target==root.data
     
        return self.hasPathSum(root.left,target-root.data) or self.hasPathSum(root.right,target-root.data)