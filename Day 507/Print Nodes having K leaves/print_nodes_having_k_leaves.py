class Solution:
    def btWithKleaves(self, root, k):
        res = []
        
        def dfs(node):
            
            if not node:
                return 0
             
            leafs_left = dfs(node.left)
            leafs_right = dfs(node.right)
            
            if leafs_left + leafs_right == k:
                res.append(node.data)
            
            if not node.left and not node.right:
                return 1
            
            return leafs_left + leafs_right
            
        dfs(root) 
        return res if res else [-1]