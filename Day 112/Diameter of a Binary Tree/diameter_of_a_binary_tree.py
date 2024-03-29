class Solution:
    
    def dia_calc(self,root):
        
        if root is None:
            return [0,0]
        
        left = self.dia_calc(root.left)
        right = self.dia_calc(root.right)
        
        op1 = left[0]
        op2 = right[0]
        op3 = left[1] + 1 + right[1]
        
        
        return [max(op1,op2,op3), max(left[1],right[1]) + 1]
    
    def diameter(self,root):
        
        return self.dia_calc(root)[0]