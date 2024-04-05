class Solution:
    def findMaxForN(self, root, n):
        
        self.req = -1
        self.temp = False
        def f(root):
            if root == None:
                return 
            f(root.left)
            if root.key > n:
                self.temp = True
                return 
            self.req = root.key
            f(root.right)
        f(root)
        
        return self.req