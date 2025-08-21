class Solution:
    def getCount(self, root, l, h):
        if root is None:
            return 0

        if root.data <= h and root.data >= l:
            return 1 + self.getCount(root.left, l, h) \
                      + self.getCount(root.right, l, h)

        
        elif root.data < l:
            return self.getCount(root.right, l, h)

        
        else:
            return self.getCount(root.left, l, h)