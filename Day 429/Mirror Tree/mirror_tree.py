class Solution:
    def mirror(self, root):
        if not root or(not root.left and not root.right):
            return
        root.left,root.right=root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)