class Solution:
    def printPaths(self, root, sum):
        
        def solve(x, y, z):
            if x:
                z = z+[x.data]
                
                if x.data == y:
                    res.append(z)
                
                solve(x.left, y-x.data, z)
                solve(x.right, y-x.data, z)
                
        res = []
        solve(root, sum, [])
        return res