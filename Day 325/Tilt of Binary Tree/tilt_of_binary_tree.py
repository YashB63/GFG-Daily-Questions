class Solution:
    def tiltTree(self,root):
        total_tilt = 0
        
        def helper(node):
            nonlocal total_tilt
            if not node:
                return 0
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            
            current_tilt = abs(left_sum - right_sum)
            total_tilt += current_tilt
            
            return left_sum + right_sum + node.data
        
        helper(root)
        return total_tilt