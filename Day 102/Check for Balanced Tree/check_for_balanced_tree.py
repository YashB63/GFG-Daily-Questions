class Solution:
    def isBalanced(self,root):
        
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        
        if not root:
            return True
        return abs(getDepth(root.left) - getDepth(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        