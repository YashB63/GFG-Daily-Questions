class Solution:
    def findMaxFork(self, root, k):
        if root == None:
            return -1
        if root.data == k:
            return k

        elif root.data < k:
            ans = self.findMaxFork(root.right, k)
            if ans == -1:
                return root.data
            else:
                return ans

        elif root.data > k:
            return self.findMaxFork(root.left, k)