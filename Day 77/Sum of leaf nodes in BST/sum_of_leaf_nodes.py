class Solution:
    def sumOfLeafNodes(self, root):
        
        if not root:
            return 0
        else:
            if not root.left and not root.right:
                return root.data
            else:
                return self.sumOfLeafNodes(root.left) + self.sumOfLeafNodes(root.right)
