class Solution:
    def preorderUtil(self, root, res):
        if root is None:
            return
        res.append(root.data)  
        self.preorderUtil(root.left, res)  
        self.preorderUtil(root.right, res)  

    def preorder(self, root):
        res = []
        self.preorderUtil(root, res)
        return res