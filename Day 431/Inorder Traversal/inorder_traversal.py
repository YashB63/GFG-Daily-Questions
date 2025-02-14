class Solution:
    def inOrder(self,root):
        res = []
        if root is None:
            return []
        res.extend(self.inOrder(root.left))
        res.append(root.data)
        res.extend(self.inOrder(root.right))
        
        return res