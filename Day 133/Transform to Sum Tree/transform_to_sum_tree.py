class Solution:
    def toSumTree(self, root) :
        
        if not root:
            return 0
        temp = root.data

        left = self.toSumTree(root.left) 
        right = self.toSumTree(root.right) 
        
        root.data = left + right
        return temp+left+right