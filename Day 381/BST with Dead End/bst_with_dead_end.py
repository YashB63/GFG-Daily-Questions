class Solution:
    def isDeadEnd(self, root, minn = 1, maxx = float('inf')):
        if not root:
            return False
        
        if minn == maxx:
            return True
            
        return self.isDeadEnd(root.left, minn = minn, maxx = root.data - 1) \
               or self.isDeadEnd(root.right, minn = root.data + 1, maxx = maxx)