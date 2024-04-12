class Solution:
    def kthLargest(self,root, k):
        
        l = []
        def inorder(x):
            if not x: return 
            inorder(x.left)
            l.append(x.data)
            inorder(x.right)
            
        inorder(root)
        return l[-k]