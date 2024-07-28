class Solution:
    def largestBst(self, root):
        def fun(node):
            if not node:
                return True, 0, float("inf"), float("-inf")
            
            left, lsize, lmin, lmax = fun(node.left)
            right, rsize, rmin, rmax = fun(node.right)
            
            if left and right and lmax<node.data<rmin:
                return True, 1+lsize+rsize, min(lmin, node.data), max(node.data, rmax)
            return False, max(lsize, rsize), 0, 0
        
        return fun(root)[1]