class Solution:
    def printNearNodes(self, root, low, high):
        if not root:
            return []
        def inorder(root,r):
            
            if root:
                inorder(root.left,r)
                r.append(root.data)
                inorder(root.right,r)
        r=[]
        inorder(root,r)
        x=[]
        if len(r)==0:
            return []
        for i in r:
            if i>=low and i<=high:
                x.append(i)
        return x