class Solution:
    def findTarget(self, root, target): 
        s = set()
        
        def fun(root):
            if root == None:
                return False
            if target - root.data in s:
                return True
                
            s.add(root.data)
            
            return fun(root.left) or fun(root.right)
            
        
        return fun(root)