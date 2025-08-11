class Solution:
    def preorder(self, root1, root2, lvl):
        if root1 is None or root2 is None:
            return

        if lvl % 2 == 0:
            t = root1.data
            root1.data = root2.data
            root2.data = t

        self.preorder(root1.left, root2.right, lvl + 1)
        self.preorder(root1.right, root2.left, lvl + 1)

    def reverseAlternate(self, root):
        self.preorder(root.left, root.right, 0)