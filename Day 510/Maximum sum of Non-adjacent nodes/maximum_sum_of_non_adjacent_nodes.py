class Solution:
    def getMaxSum(self, root):
        def solve(node):
            if not node:
                return (0,0)
                
            left=solve(node.left)
            right=solve(node.right)
            
            include=node.data+left[1]+right[1]
            exclude=max(left)+max(right)
            
            return (include,exclude)
            
            
        include,exclude=solve(root)
        return max (include,exclude)