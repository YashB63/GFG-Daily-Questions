class Solution:
    def maxPathSum(self, root):
        if (root == None):
            return None
        a = self.maxPathSum(root.left)
        b = self.maxPathSum(root.right)
        if (a == None) and (b== None):
            return root.data
        elif (a == None):
            return b + root.data
        elif (b == None):
            return a + root.data
        else:
            return max(a,b) + root.data