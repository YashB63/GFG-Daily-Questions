class Solution:
    def dfs(self, root, mini, maxi):
        if root is None:
            return False

        if root.left is None and root.right is None and mini == maxi:
            return True

        return (self.dfs(root.left, mini, root.data - 1)
                or self.dfs(root.right, root.data + 1, maxi))

    def isDeadEnd(self, root):
        return self.dfs(root, 1, float('inf'))