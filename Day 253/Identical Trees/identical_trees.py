class Solution:
    def isIdentical(self,root1, root2):
        if not root1 and not root2:
            return True 
        if not root1 or not root2: 
            return False 
        if root1.data != root2.data:
            return False 
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
