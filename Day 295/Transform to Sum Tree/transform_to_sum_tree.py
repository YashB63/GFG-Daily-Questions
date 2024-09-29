class Solution:
    def toSumTree(self, root) :
        def solve(root):
            
            if root is None:
                return 0
            left=solve(root.left)
            right=solve(root.right)
            old_value = root.data
            root.data=left+right
            return old_value + root.data
        solve(root)