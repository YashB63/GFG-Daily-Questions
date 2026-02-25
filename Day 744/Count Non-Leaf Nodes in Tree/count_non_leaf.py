class Solution:
    def _count(self, root, a):
        if not root: return 
        
        if root and (root.left or root.right):
            a[0] += 1
        self._count(root.left, a)
        self._count(root.right,a)
        
    
    def countNonLeafNodes(self, root):
        a = [0]
        self._count(root, a)
        return a[0]