class Solution:
    def lca(self,root, n1, n2):
        if root is None or root.data == n1 or root.data == n2:
            return root

        left_lca = self.lca(root.left, n1, n2)
        right_lca = self.lca(root.right, n1, n2)

        if left_lca and right_lca:
            return root

        if left_lca:
            return left_lca
        return right_lca