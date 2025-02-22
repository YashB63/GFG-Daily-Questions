class Solution:
    def LCA(self, root, n1, n2):
        if not root:
            return None
        
        if n1.data < root.data and n2.data < root.data:
            return self.LCA(root.left,n1,n2)
        
        if n1.data > root.data and n2.data > root.data:
            return self.LCA(root.right,n1,n2)

        return root