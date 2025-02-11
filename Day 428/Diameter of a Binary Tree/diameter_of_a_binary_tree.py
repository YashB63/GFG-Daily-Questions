class Solution:
    def diameter(self, root):
        def f(root):
            if not root:
                return 0
            
            l = f(root.left)
            r = f(root.right)
            
            ans[0] = max(ans[0], l + r)
            v = 1 + max(l, r)
            return v
        ans = [0]
        f(root)
        return ans[0]