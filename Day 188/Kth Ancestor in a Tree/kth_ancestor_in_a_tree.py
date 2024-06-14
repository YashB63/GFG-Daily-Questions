def kthAncestor(root,k, node):
    
    def solve(root,node):
        global k
        
        if root is None:
            return 
            
        if root.data == node:
            return root
            
        left = solve(root.left, node)
        right = solve(root.right, node)
        
        if left is not None and right is None:
            k = k-1
            if k <=0:
                k = 999
                return root
            return left
            
        if right is not None and left is None:
            k = k-1
            if k <=0:
                k = 999
                return root
            return right
        
    ans = solve(root,node)
    if ans is None or ans.data == node:
        return -1
    else:
        return ans.data