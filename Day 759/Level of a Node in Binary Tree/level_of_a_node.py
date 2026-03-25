class Solution:
    def getLevel(self, root, target):
        def fun(node, target, level):
            if not node or self.res:
                return
            
            if node.data==target:
                self.res = level
                return
            
            fun(node.left, target, level+1)
            fun(node.right, target, level+1)
        
        self.res = 0
        fun(root, target, 1)
        return self.res