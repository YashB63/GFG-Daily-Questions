class Solution:
    def __init__(self):
        self.count = 0  

    def subtreeSum(self, root, x):
        if root is None:
            return 0  

        left_sum = self.subtreeSum(root.left, x)
        right_sum = self.subtreeSum(root.right, x)

        total_sum = left_sum + right_sum + root.data

        if total_sum == x:
            self.count += 1

        return total_sum  

    def countSubtrees(self, root, x):
        self.count = 0
        self.subtreeSum(root, x)
        return self.count