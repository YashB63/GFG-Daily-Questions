class Solution:
    def is_sum_tree(self, node):
        flag = True
        def sumtree(root):
            nonlocal flag
            if not root: return 0
            if not root.left and not root.right: return root.data
            
            right_sum = sumtree(root.right)
            left_sum = sumtree(root.left)
            if root.data != left_sum + right_sum:
                flag = False
                
            return root.data+left_sum+right_sum
                
        sumtree(node)
        return flag