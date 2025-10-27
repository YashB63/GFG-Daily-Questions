class Solution:
    def removekeys(self, root, l, r):
        if root is None:
            return None

        left = self.removekeys(root.left, l, r)
        right = self.removekeys(root.right, l, r)

        if l <= root.data <= r:
            root.left = left
            root.right = right
            return root

        elif root.data < l:
            return right

        else:
            return left