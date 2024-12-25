class Solution:
    def findMaxSum(self, root): 
        if not root:
            return 0
        self.res = float('-inf')
        
        def solve(node):
            if not node:
                return 0
            left=solve(node.left)
            right=solve(node.right)
            
            temp = max(max(left,right)+node.data,node.data)
            ans = max(temp,left+right+node.data)
            self.res = max(self.res,ans)
            return temp
            
        solve(root)
        return(self.res)