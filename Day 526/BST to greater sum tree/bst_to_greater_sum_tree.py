class Solution:
    def get_sum(self, root):
        if root == None:
            return 0
        return root.data + self.get_sum(root.left) + self.get_sum(root.right)
    
    def transformTreeUtil(self, root, sm):
        if root == None:
            return sm
    
        l = self.transformTreeUtil(root.left, sm)
        
        val = root.data
        root.data = total - l - root.data
        
        r = self.transformTreeUtil(root.right, val + l)
        return r
    
    def transformTree(self, root):
        global total
        total = self.get_sum(root)
        self.transformTreeUtil(root,0)