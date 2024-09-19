class Solution:
    def mirror(self,root):
        if root is None:
            return
        self.mirror(root.left) 
        self.mirror(root.right)
        root.left, root.right = root.right, root.left

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)