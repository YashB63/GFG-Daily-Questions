class Solution:
    
    def deleteNode(self, root, k):
        if not root:
            return None
        if root.data < k:
            root.right = self.deleteNode(root.right, k)
            return root
        else:
            if root.left:
                return self.deleteNode(root.left, k)
            return None