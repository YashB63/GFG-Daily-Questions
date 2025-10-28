class Solution:
    def updateTree(self, root, sum):
        if root is None:
            return

        self.updateTree(root.right, sum)

        sum[0] += root.data
        root.data = sum[0] - root.data

        self.updateTree(root.left, sum)

    def transformTree(self, root):
        sum = [0]
        self.updateTree(root, sum)