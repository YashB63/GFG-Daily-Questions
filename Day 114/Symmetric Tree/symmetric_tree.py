class Solution:
    
    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None or root1.data !=root2.data:
            return False
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
    def isSymmetric(self, root):
        
        if root == None:
            return True
        return self.isMirror(root.left, root.right)