class Solution:
    res = -999999999

    def maxPathSumUtil(self, root):
        global res  

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        ls = self.maxPathSumUtil(root.left)
        rs = self.maxPathSumUtil(root.right)

        if root.left and root.right:
            res = max(res, ls + rs + root.data)
            return max(ls, rs) + root.data

        if root.left is None:
            return rs + root.data
        else:
            return ls + root.data

    def maxPathSum(self, root):
        global res
        res = -999999999

        h = self.maxPathSumUtil(root)

        if root.left is None:
            res = max(res, h)
        if root.right is None:
            res = max(res, h)

        return res  