class Solution:
    def isSumTree(self,root):
        
        def sam(root):
            if root is None or ((root.left is None) and (root.right is None)) :
                return True
            a=dam(root.left)
            b=dam(root.right)
            if (a+b==root.data and sam(root.left) and sam(root.right)):
                return True
            return False
        def dam(root):
            if root is None:
                return 0
            else:
                return dam(root.left)+root.data+dam(root.right)
                
        return sam(root)