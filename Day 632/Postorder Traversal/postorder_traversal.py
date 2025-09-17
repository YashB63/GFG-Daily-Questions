class Solution:
    def postOrderUtil(self, root, res):
        if root is None:
            return

        self.postOrderUtil(root.left, res)

        self.postOrderUtil(root.right, res)

        res.append(root.data)

    def postOrder(self, root):
        res = []
        self.postOrderUtil(root, res)  
        return res