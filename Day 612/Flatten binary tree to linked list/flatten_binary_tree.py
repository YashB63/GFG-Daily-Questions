class Solution:
    def flatten(self, root):
        if root==None or (not root.left and not root.right):
            return
        else :
            if root.left:
                self.flatten(root.left)
                temp=root.right
                
                root.right=root.left
                root.left=None
                t=root.right
                while t.right:
                    t=t.right
                t.right=temp
                    
            self.flatten(root.right)