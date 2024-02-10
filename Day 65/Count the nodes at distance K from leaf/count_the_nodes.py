class Solution:
    def recur(self, root, lvl, k, res, s1):
        if root == None:
            return
        res.append(root)
        if root.left == None and root.right == None:
            index = lvl - k
            if index >= 0:
                s1.add(res[index])
            return
        self.recur(root.left, lvl + 1, k, res.copy(), s1)
        self.recur(root.right, lvl + 1, k, res.copy(), s1)
        
    
    def printKDistantfromLeaf(self, root, k):
        
        s1 = set()
        res = []
        self.recur(root, 0, k, res.copy(), s1)
        return len(s1)